![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-blue?logo=githubactions)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![Terraform](https://img.shields.io/badge/Terraform-IaC-purple?logo=terraform)
![Python](https://img.shields.io/badge/Python-Application-yellow?logo=python)
![OWASP ZAP](https://img.shields.io/badge/OWASP_ZAP-DAST-red)

# Cloud DevSecOps Security Pipeline

A hands-on DevSecOps pipeline project focused on integrating automated security controls into the software development lifecycle (SDLC) using GitHub Actions.

This project demonstrates how multiple security scanning technologies can be orchestrated together to identify and remediate security issues across source code, dependencies, containers, infrastructure-as-code (IaC), and running applications.

---

## Security Controls Implemented

| Security Layer | Tool Used | Purpose |
|---|---|---|
| Secrets Detection | Gitleaks | Detect hardcoded secrets and sensitive data |
| Dependency Scanning | Trivy | Detect vulnerable application dependencies |
| Static Application Security Testing (SAST) | Semgrep | Detect insecure coding patterns |
| Container Security Scanning | Trivy | Scan Docker images for OS/library vulnerabilities |
| Infrastructure as Code (IaC) Scanning | Checkov | Detect insecure Terraform configurations |
| Dynamic Application Security Testing (DAST) | OWASP ZAP | Scan running web application for security weaknesses |

---

## Technologies Used

- GitHub Actions
- Docker
- Python
- Flask
- Terraform
- Gitleaks
- Trivy
- Semgrep
- Checkov
- OWASP ZAP

---

## DevSecOps Pipeline Flow

1. Developer pushes code to GitHub
2. GitHub Actions pipeline starts automatically
3. Secrets scanning executes
4. Dependency vulnerability scanning executes
5. SAST analysis executes
6. Container image scanning executes
7. IaC security scanning executes
8. DAST security validation executes
9. Pipeline passes or fails based on security findings

---

## Security Scenarios Demonstrated

This project intentionally introduced and remediated multiple security issues, including:

- Hardcoded secrets
- Vulnerable dependencies
- Command injection risks
- Insecure Flask configurations
- Container vulnerabilities
- Overly permissive Terraform configurations
- Missing HTTP security headers

---

## Project Goals

- Demonstrate layered DevSecOps security controls
- Practice shift-left security principles
- Simulate enterprise CI/CD security gates
- Learn remediation workflows
- Build practical cloud security engineering skills

---

## Repository Structure

```text
.github/workflows/       # GitHub Actions pipeline
app/                     # Flask demo application
config/                  # Security configuration files
docs/screenshots/        # Project screenshots
terraform-insecure-demo/ # Intentionally insecure Terraform examples
terraform-secure/        # Future remediated Terraform configurations
```

---

## Current Status

- Secret scanning implemented
- Dependency scanning implemented
- SAST implemented
- Container scanning implemented
- DAST validated locally
- IaC scanning implemented
- Pipeline enforcement enabled
- Security remediation workflows tested

---

## Future Improvements

- Full CI-integrated DAST automation
- Hardened production Docker image
- Secure Terraform deployment examples
- GitHub branch protection policies
- Security reporting dashboards
- SBOM generation
- Artifact signing and verification
