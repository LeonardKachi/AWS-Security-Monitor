import boto3
import json

# Initialize AWS Clients
ec2 = boto3.client('ec2')
iam = boto3.client('iam')
s3 = boto3.client('s3')
securityhub = boto3.client('securityhub')

def check_security_groups():
    """Checks for security groups with open ports (0.0.0.0/0)."""
    findings = []
    response = ec2.describe_security_groups()
    
    for sg in response['SecurityGroups']:
        for rule in sg.get('IpPermissions', []):
            for ip in rule.get('IpRanges', []):
                if ip['CidrIp'] == '0.0.0.0/0':
                    findings.append(f"⚠ Security Group '{sg['GroupId']}' allows inbound {rule['IpProtocol']} access from ANYWHERE.")
    
    return findings

def check_iam_users():
    """Checks IAM users without MFA enabled."""
    findings = []
    response = iam.list_users()
    
    for user in response['Users']:
        mfa_response = iam.list_mfa_devices(UserName=user['UserName'])
        if not mfa_response['MFADevices']:
            findings.append(f"⚠ IAM User '{user['UserName']}' does NOT have MFA enabled.")
    
    return findings

def check_s3_encryption():
    """Checks for unencrypted S3 buckets."""
    findings = []
    response = s3.list_buckets()
    
    for bucket in response['Buckets']:
        try:
            enc_response = s3.get_bucket_encryption(Bucket=bucket['Name'])
        except s3.exceptions.ClientError:
            findings.append(f"⚠ S3 Bucket '{bucket['Name']}' is NOT encrypted.")
    
    return findings

def check_security_hub_findings():
    """Fetches AWS Security Hub findings."""
    findings = []
    try:
        response = securityhub.get_findings()
        for finding in response.get('Findings', []):
            findings.append(f"🛑 Security Hub Finding: {finding['Title']} - {finding['Description']}")
    except securityhub.exceptions.ClientError:
        findings.append("⚠ AWS Security Hub is not enabled.")
    
    return findings

def generate_report():
    """Generates a security audit report."""
    report = {
        "SecurityGroups": check_security_groups(),
        "IAMUsers": check_iam_users(),
        "S3Buckets": check_s3_encryption(),
        "SecurityHubFindings": check_security_hub_findings()
    }

    with open("aws_security_report.json", "w") as f:
        json.dump(report, f, indent=4)
    
    print("✅ Security audit completed. Report saved to 'aws_security_report.json'.")

if _name_ == "_main_":
    generate_report()