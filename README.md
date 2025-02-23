# Automated AWS Security Monitoring

A *Python-based AWS security tool* that automates security monitoring, identifying vulnerabilities in AWS environments and *reducing security audit time by 50%*.

## 🚀 Features  
✅ *Security Group Analysis* – Detects open ports allowing unrestricted access.  
✅ *IAM Security Check* – Identifies IAM users without MFA enabled.  
✅ *S3 Bucket Security* – Flags unencrypted S3 buckets.  
✅ *AWS Security Hub Integration* – Fetches existing security findings.  
✅ *Automated Security Report* – Saves findings in a structured JSON file.  

## 🛠 Technologies Used  
- *Python*  
- *AWS SDK (Boto3)*  
- *AWS Security Hub*  
- *IAM & S3 Security Checks*  
- *JSON Reporting*  

## 📥 Installation  
Clone the repository and install dependencies:  

```bash
git clone https://github.com/LeonardKachi/aws-security-monitoring.git
```
cd aws-security-monitoring
pip install -r requirements.txt

## ⚙ AWS Configuration

Ensure your **AWS credentials** are set up:
```
aws configure
```
you’ll need to provide:
	•	AWS Access Key
	•	AWS Secret Key
	•	Default region (e.g., us-east-1)

## ▶ Usage

Run the script to start an AWS security audit:
```
python aws_security_monitor.py
```
The script will check security groups, IAM users, S3 buckets, and Security Hub findings. A security report will be saved as aws_security_report.json.

## 📊 Example Output (JSON Report)
```
{
    "SecurityGroups": [
        "⚠ Security Group 'sg-12345' allows inbound SSH access from ANYWHERE."
    ],
    "IAMUsers": [
        "⚠ IAM User 'admin' does NOT have MFA enabled."
    ],
    "S3Buckets": [
        "⚠ S3 Bucket 'my-unsecured-bucket' is NOT encrypted."
    ],
    "SecurityHubFindings": [
        "🛑 Security Hub Finding: Root account has active access keys - This is a critical security risk."
    ]
}
```
## 📌 Future Improvements
• ✅ AWS Lambda support for real-time security monitoring<br>
• ✅ Email/SMS notifications for critical vulnerabilities<br>
• ✅ Integration with AWS Config for continuous compliance<br>

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📜 License

This project is licensed under the MIT License.


