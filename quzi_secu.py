# --- 80-Question Multiple-Choice Exam ---

def run_quiz():
    quiz = [
        # --- Topic 1: Security in Cloud Computing and Virtualization (Q1-Q20) ---
        {
            "topic": "Security in Cloud Computing and Virtualization",
            "question": "1. Cloud computing offers on-demand access to scalable resources, reducing costs, and enabling:",
            "options": {
                "A": "flexible resources",
                "B": "economies of scale",
                "C": "global collaboration",
                "D": "faster innovation"
            },
            "answer": "C",
            "explanation": "Cloud computing offers on-demand access to scalable resources, reducing costs, and enabling global collaboration."
        },
        {
            "topic": "Security in Cloud Computing and Virtualization",
            "question": "2. The delivery of computing services—such as servers, storage, databases, networking, software, and analytics—over the internet ('the cloud') is known as:",
            "options": {
                "A": "Virtualization",
                "B": "Cloud Computing",
                "C": "Application Virtualization",
                "D": "Hybrid Cloud"
            },
            "answer": "B",
            "explanation": "The delivery of computing services—such as servers, storage, databases, networking, software, and analytics—over the internet ('the cloud') to offer faster innovation, flexible resources, and economies of scale."
        },
        {
            "topic": "Security in Cloud Computing and Virtualization",
            "question": "3. Which of the following is an example of a Cloud Service Model that provides a platform allowing customers to develop, run, and manage applications without managing infrastructure?",
            "options": {
                "A": "Infrastructure as a Service (IaaS)",
                "B": "Software as a Service (SaaS)",
                "C": "Platform as a Service (PaaS)",
                "D": "Public Cloud"
            },
            "answer": "C",
            "explanation": "Platform as a Service (PaaS): Provides a platform allowing customers to develop, run, and manage applications without managing infrastructure."
        },
        {
            "topic": "Security in Cloud Computing and Virtualization",
            "question": "4. Which of the following is an example of a Cloud Service Model that delivers software applications over the internet on a subscription basis?",
            "options": {
                "A": "Infrastructure as a Service (IaaS)",
                "B": "Platform as a Service (PaaS)",
                "C": "Software as a Service (SaaS)",
                "D": "Hybrid Cloud"
            },
            "answer": "C",
            "explanation": "Software as a Service (SaaS): Delivers software applications over the internet on a subscription basis."
        },
        {
            "topic": "Security in Cloud Computing and Virtualization",
            "question": "5. Which Cloud Deployment Model is characterized by services offered over the public internet and available to everyone?",
            "options": {
                "A": "Private Cloud",
                "B": "Hybrid Cloud",
                "C": "Public Cloud",
                "D": "OS-Level Virtualization"
            },
            "answer": "C",
            "explanation": "Public Cloud: Services offered over the public internet and available to everyone."
        },
        {
            "topic": "Security in Cloud Computing and Virtualization",
            "question": "6. Cloud infrastructure operated solely for one organization describes which deployment model?",
            "options": {
                "A": "Hybrid Cloud",
                "B": "Public Cloud",
                "C": "Private Cloud",
                "D": "Application Virtualization"
            },
            "answer": "C",
            "explanation": "Private Cloud: Cloud infrastructure operated solely for one organization."
        },
        {
            "topic": "Security in Cloud Computing and Virtualization",
            "question": "7. What is the process of creating a virtual version of something, such as a server, storage device, network, or operating system?",
            "options": {
                "A": "Virtualization",
                "B": "Cloud Computing",
                "C": "Hypervisor Security",
                "D": "Continuous Monitoring"
            },
            "answer": "A",
            "explanation": "Virtualization: The process of creating a virtual version of something, such as a server, storage device, network, or operating system."
        },
        {
            "topic": "Security in Cloud Computing and Virtualization",
            "question": "8. What allows multiple virtual systems, called virtual machines (VMs), to run on a single hardware platform independently?",
            "options": {
                "A": "Application Virtualization",
                "B": "Virtualization",
                "C": "Public Cloud",
                "D": "Strong Identity and Access Management"
            },
            "answer": "B",
            "explanation": "Allows multiple virtual systems, called virtual machines (VMs), to run on a single hardware platform independently."
        },
        {
            "topic": "Security in Cloud Computing and Virtualization",
            "question": "9. Which type of virtualization creates fully isolated virtual machines that emulate physical hardware?",
            "options": {
                "A": "Application Virtualization",
                "B": "OS-Level Virtualization (Containerization)",
                "C": "Hardware Virtualization (Full Virtualization)",
                "D": "Private Cloud"
            },
            "answer": "C",
            "explanation": "Hardware Virtualization (Full Virtualization) - Creates fully isolated virtual machines that emulate physical hardware."
        },
        {
            "topic": "Security in Cloud Computing and Virtualization",
            "question": "10. Which type of virtualization virtualizes applications rather than the whole OS or hardware?",
            "options": {
                "A": "OS-Level Virtualization (Containerization)",
                "B": "Hardware Virtualization (Full Virtualization)",
                "C": "Application Virtualization",
                "D": "Infrastructure as a Service (IaaS)"
            },
            "answer": "C",
            "explanation": "Application Virtualization - Virtualizes applications rather than the whole OS or hardware."
        },
        {
            "topic": "Security in Cloud Computing and Virtualization",
            "question": "11. Sensitive data stored in cloud environments can be exposed due to unauthorized access, leading to which security challenge?",
            "options": {
                "A": "Misconfigurations",
                "B": "Hypervisor Attacks",
                "C": "Data Breaches",
                "D": "Strong Identity and Access Management (IAM)"
            },
            "answer": "C",
            "explanation": "Data Breaches - Sensitive data stored in cloud environments can be exposed due to unauthorized access."
        },
        {
            "topic": "Security in Cloud Computing and Virtualization",
            "question": "12. Misconfigured cloud resources (e.g., storage buckets, virtual networks) are one of the leading causes of security incidents, known as:",
            "options": {
                "A": "Data Breaches",
                "B": "Misconfigurations",
                "C": "Hypervisor Attacks",
                "D": "Container Security"
            },
            "answer": "B",
            "explanation": "Misconfigurations - Misconfigured cloud resources (e.g., storage buckets, virtual networks) are one of the leading causes of security incidents."
        },
        {
            "topic": "Security in Cloud Computing and Virtualization",
            "question": "13. Since hypervisors control multiple virtual machines, attacks targeting the hypervisor can compromise all VMs on a host. This challenge is called:",
            "options": {
                "A": "Data Breaches",
                "B": "Misconfigurations",
                "C": "Hypervisor Attacks",
                "D": "Network Security"
            },
            "answer": "C",
            "explanation": "Hypervisor Attacks - Since hypervisors control multiple virtual machines, attacks targeting the hypervisor can compromise all VMs on a host."
        },
        {
            "topic": "Security in Cloud Computing and Virtualization",
            "question": "14. Implementing least privilege access and multi-factor authentication is part of which security solution?",
            "options": {
                "A": "Encryption",
                "B": "Network Security",
                "C": "Strong Identity and Access Management (IAM)",
                "D": "Patch Management"
            },
            "answer": "C",
            "explanation": "Strong Identity and Access Management (IAM): Implement least privilege access and multi-factor authentication."
        },
        {
            "topic": "Security in Cloud Computing and Virtualization",
            "question": "15. The practice of encrypting data at rest and in transit using strong cryptographic algorithms is:",
            "options": {
                "A": "Patch Management",
                "B": "Encryption",
                "C": "Secure Configuration",
                "D": "Hypervisor Security"
            },
            "answer": "B",
            "explanation": "Encryption: Encrypt data at rest and in transit using strong cryptographic algorithms."
        },
        {
            "topic": "Security in Cloud Computing and Virtualization",
            "question": "16. Which security solution involves using segmentation, firewalls, VPCs, and monitoring with IDS/IPS?",
            "options": {
                "A": "Strong Identity and Access Management (IAM)",
                "B": "Network Security",
                "C": "Container Security",
                "D": "Backup & Disaster Recovery"
            },
            "answer": "B",
            "explanation": "Network Security: Use segmentation, firewalls, VPCs, and monitoring with IDS/IPS."
        },
        {
            "topic": "Security in Cloud Computing and Virtualization",
            "question": "17. What is the practice of keeping hypervisors, OS, and apps up to date with security patches?",
            "options": {
                "A": "Secure Configuration",
                "B": "Continuous Monitoring",
                "C": "Patch Management",
                "D": "Hypervisor Security"
            },
            "answer": "C",
            "explanation": "Patch Management: Keep hypervisors, OS, and apps up to date with security patches."
        },
        {
            "topic": "Security in Cloud Computing and Virtualization",
            "question": "18. Harden hypervisors, disable unnecessary services, and limit access are parts of which security solution?",
            "options": {
                "A": "Patch Management",
                "B": "Container Security",
                "C": "Hypervisor Security",
                "D": "Incident Response & Forensics"
            },
            "answer": "C",
            "explanation": "Hypervisor Security: Harden hypervisors, disable unnecessary services, and limit access."
        },
        {
            "topic": "Security in Cloud Computing and Virtualization",
            "question": "19. Regularly back up data and test recovery procedures are parts of which best practice?",
            "options": {
                "A": "Container Security",
                "B": "Incident Response & Forensics",
                "C": "Backup & Disaster Recovery",
                "D": "Encryption"
            },
            "answer": "C",
            "explanation": "Backup & Disaster Recovery: Regularly back up data and test recovery procedures."
        },
        {
            "topic": "Security in Cloud Computing and Virtualization",
            "question": "20. What is an example of a cloud service listed in the reviewer text?",
            "options": {
                "A": "Terraform",
                "B": "Microsoft Azure",
                "C": "SIEM",
                "D": "IDS/IPS"
            },
            "answer": "B",
            "explanation": "Examples of Cloud Services: Amazon Web Services (AWS), Microsoft Azure, Google Cloud Platform (GCP)."
        },

        # --- Topic 2: Information Assurance and Security (Q21-Q40) ---
        {
            "topic": "Information Assurance and Security",
            "question": "21. Compliance with recognized regulations and standards is critical in achieving information assurance and fostering:",
            "options": {
                "A": "confidentiality",
                "B": "trust",
                "C": "availability",
                "D": "integrity"
            },
            "answer": "B",
            "explanation": "Compliance with recognized regulations and standards (GDPR, HIPAA, ISO/IEC 27001) is critical in achieving information assurance and fostering trust."
        },
        {
            "topic": "Information Assurance and Security",
            "question": "22. The General Data Protection Regulation (GDPR) became effective across all EU member states on:",
            "options": {
                "A": "1996",
                "B": "May 25, 2018",
                "C": "2003",
                "D": "2005"
            },
            "answer": "B",
            "explanation": "Comprehensive data protection law effective May 25, 2018, across all EU member states."
        },
        {
            "topic": "Information Assurance and Security",
            "question": "23. One objective of GDPR is to protect individual privacy rights and give individuals greater control over:",
            "options": {
                "A": "health insurance",
                "B": "personal data",
                "C": "information assets",
                "D": "Business Associate Agreements (BAAs)"
            },
            "answer": "B",
            "explanation": "Objectives: Protect individual privacy rights and give individuals greater control over personal data."
        },
        {
            "topic": "Information Assurance and Security",
            "question": "24. Which GDPR principle requires that data must be processed legally, fairly, and clearly communicated?",
            "options": {
                "A": "Purpose Limitation",
                "B": "Data Minimization",
                "C": "Lawfulness, Fairness, and Transparency",
                "D": "Accountability"
            },
            "answer": "C",
            "explanation": "Lawfulness, Fairness, and Transparency: Data must be processed legally, fairly, and clearly communicated."
        },
        {
            "topic": "Information Assurance and Security",
            "question": "25. The GDPR principle that requires data collected only for specific and legitimate purposes is:",
            "options": {
                "A": "Accuracy",
                "B": "Purpose Limitation",
                "C": "Storage Limitation",
                "D": "Integrity and Confidentiality"
            },
            "answer": "B",
            "explanation": "Purpose Limitation: Data collected only for specific and legitimate purposes."
        },
        {
            "topic": "Information Assurance and Security",
            "question": "26. Which GDPR principle requires organizations to collect only necessary data for intended purposes?",
            "options": {
                "A": "Data Minimization",
                "B": "Storage Limitation",
                "C": "Accuracy",
                "D": "Accountability"
            },
            "answer": "A",
            "explanation": "Data Minimization: Collect only necessary data for intended purposes."
        },
        {
            "topic": "Information Assurance and Security",
            "question": "27. Keeping personal data accurate and up to date is required by which GDPR principle?",
            "options": {
                "A": "Purpose Limitation",
                "B": "Lawfulness, Fairness, and Transparency",
                "C": "Accuracy",
                "D": "Integrity and Confidentiality"
            },
            "answer": "C",
            "explanation": "Accuracy: Keep personal data accurate and up to date."
        },
        {
            "topic": "Information Assurance and Security",
            "question": "28. The GDPR principle to Retain data only as long as needed for its purpose is:",
            "options": {
                "A": "Accountability",
                "B": "Data Minimization",
                "C": "Storage Limitation",
                "D": "Purpose Limitation"
            },
            "answer": "C",
            "explanation": "Storage Limitation: Retain data only as long as needed for its purpose."
        },
        {
            "topic": "Information Assurance and Security",
            "question": "29. Protecting data against unauthorized access, alteration, or destruction is the goal of which GDPR principle?",
            "options": {
                "A": "Accuracy",
                "B": "Integrity and Confidentiality",
                "C": "Lawfulness, Fairness, and Transparency",
                "D": "Accountability"
            },
            "answer": "B",
            "explanation": "Integrity and Confidentiality: Protect data against unauthorized access, alteration, or destruction."
        },
        {
            "topic": "Information Assurance and Security",
            "question": "30. Which GDPR principle requires Organizations must demonstrate compliance with all GDPR principles?",
            "options": {
                "A": "Storage Limitation",
                "B": "Accountability",
                "C": "Data Minimization",
                "D": "Purpose Limitation"
            },
            "answer": "B",
            "explanation": "Accountability: Organizations must demonstrate compliance with all GDPR principles."
        },
        {
            "topic": "Information Assurance and Security",
            "question": "31. The U.S. federal law enacted in 1996 to protect sensitive patient health information is:",
            "options": {
                "A": "GDPR",
                "B": "ISO/IEC 27001",
                "C": "HIPAA",
                "D": "ISMS"
            },
            "answer": "C",
            "explanation": "Health Insurance Portability and Accountability Act (HIPAA): U.S. federal law enacted in 1996 to protect sensitive patient health information."
        },
        {
            "topic": "Information Assurance and Security",
            "question": "32. One of the objectives of HIPAA is to protect medical records and:",
            "options": {
                "A": "data protection laws",
                "B": "personal health data",
                "C": "compliance programs",
                "D": "information assets"
            },
            "answer": "B",
            "explanation": "Objectives: Protect medical records and personal health data."
        },
        {
            "topic": "Information Assurance and Security",
            "question": "33. Which HIPAA rule, effective in 2003, established Standards for Protected Health Information (PHI)?",
            "options": {
                "A": "Privacy Rule",
                "B": "Security Rule",
                "C": "Business Associate Agreements (BAAs)",
                "D": "Risk Assessment and Treatment"
            },
            "answer": "A",
            "explanation": "Privacy Rule (2003): Standards for Protected Health Information (PHI)."
        },
        {
            "topic": "Information Assurance and Security",
            "question": "34. The HIPAA rule, effective in 2005, which mandated Administrative, physical, and technical safeguards for electronic PHI is the:",
            "options": {
                "A": "Privacy Rule",
                "B": "Security Rule",
                "C": "Compliance Audit",
                "D": "Storage Limitation"
            },
            "answer": "B",
            "explanation": "Security Rule (2005): Administrative, physical, and technical safeguards for electronic PHI."
        },
        {
            "topic": "Information Assurance and Security",
            "question": "35. HIPAA encouraged compliance programs and:",
            "options": {
                "A": "Storage Limitation",
                "B": "Lawfulness, Fairness, and Transparency",
                "C": "Business Associate Agreements (BAAs)",
                "D": "Risk Assessment and Treatment"
            },
            "answer": "C",
            "explanation": "Impact: Encouraged compliance programs and Business Associate Agreements (BAAs)."
        },
        {
            "topic": "Information Assurance and Security",
            "question": "36. ISO/IEC 27001 is a globally recognized standard for establishing, implementing, maintaining, and continually improving an:",
            "options": {
                "A": "Protected Health Information (PHI)",
                "B": "Information Security Management System (ISMS)",
                "C": "electronic health records (EHRs)",
                "D": "Business Impact Analysis (BIA)"
            },
            "answer": "B",
            "explanation": "ISO/IEC 27001... is a globally recognized standard for establishing, implementing, maintaining, and continually improving an Information Security Management System (ISMS)."
        },
        {
            "topic": "Information Assurance and Security",
            "question": "37. ISO/IEC 27001 provides a systematic approach to ensure confidentiality, integrity, and:",
            "options": {
                "A": "trust",
                "B": "compliance",
                "C": "availability",
                "D": "Risk Assessment"
            },
            "answer": "C",
            "explanation": "Provides a systematic approach to ensure confidentiality, integrity, and availability."
        },
        {
            "topic": "Information Assurance and Security",
            "question": "38. Which Key Component of ISO/IEC 27001 involves Senior management supports the ISMS?",
            "options": {
                "A": "Risk Assessment and Treatment",
                "B": "Security Controls",
                "C": "Continuous Improvement",
                "D": "Leadership and Commitment"
            },
            "answer": "D",
            "explanation": "Leadership and Commitment: Senior management supports the ISMS."
        },
        {
            "topic": "Information Assurance and Security",
            "question": "39. The ISO/IEC 27001 Key Component 'Security Controls' is based on:",
            "options": {
                "A": "7 Key Principles",
                "B": "93 reference controls",
                "C": "5 Phases",
                "D": "Administrative safeguards"
            },
            "answer": "B",
            "explanation": "Security Controls: Based on 93 reference controls."
        },
        {
            "topic": "Information Assurance and Security",
            "question": "40. A benefit of ISO/IEC 27001 is Enhanced trust with customers and:",
            "options": {
                "A": "Business Associate Agreements (BAAs)",
                "B": "security risks",
                "C": "regulators",
                "D": "legal and contractual requirements"
            },
            "answer": "C",
            "explanation": "Benefits: Enhanced trust with customers and regulators."
        },

        # --- Topic 3: Incident Response and Disaster Recovery (Q41-Q60) ---
        {
            "topic": "Incident Response and Disaster Recovery",
            "question": "41. What is an Organized approach to handling cybersecurity incidents?",
            "options": {
                "A": "Disaster Recovery",
                "B": "Business Impact Analysis (BIA)",
                "C": "Incident Response",
                "D": "Security Auditing"
            },
            "answer": "C",
            "explanation": "Incident Response: Organized approach to handling cybersecurity incidents."
        },
        {
            "topic": "Incident Response and Disaster Recovery",
            "question": "42. Incident Response is a Structured process to swiftly identify, contain, and recover from threats ensuring:",
            "options": {
                "A": "software updates",
                "B": "minimal impact",
                "C": "Natural disasters",
                "D": "critical business functions"
            },
            "answer": "B",
            "explanation": "Structured process to swiftly identify, contain, and recover from threats ensuring minimal impact."
        },
        {
            "topic": "Incident Response and Disaster Recovery",
            "question": "43. Which phase of the NIST (SP 800-61) Incident Response process involves Planning, team setup, and communication strategies?",
            "options": {
                "A": "Detection & Analysis",
                "B": "Preparation",
                "C": "Containment, Eradication, and Recovery",
                "D": "Post-Incident Activity"
            },
            "answer": "B",
            "explanation": "Preparation: Planning, team setup, communication strategies."
        },
        {
            "topic": "Incident Response and Disaster Recovery",
            "question": "44. The NIST phase for Incident Response that involves Identify and confirm incidents is:",
            "options": {
                "A": "Preparation",
                "B": "Detection & Analysis",
                "C": "Post-Incident Activity",
                "D": "Strategy Development"
            },
            "answer": "B",
            "explanation": "Detection & Analysis: Identify and confirm incidents."
        },
        {
            "topic": "Incident Response and Disaster Recovery",
            "question": "45. Which NIST Incident Response phase involves Stop spread, remove threat, restore systems?",
            "options": {
                "A": "Post-Incident Activity",
                "B": "Detection & Analysis",
                "C": "Containment, Eradication, and Recovery",
                "D": "Risk Assessment"
            },
            "answer": "C",
            "explanation": "Containment, Eradication, and Recovery: Stop spread, remove threat, restore systems."
        },
        {
            "topic": "Incident Response and Disaster Recovery",
            "question": "46. Review lessons learned and improve describes which NIST Incident Response phase?",
            "options": {
                "A": "Preparation",
                "B": "Detection & Analysis",
                "C": "Containment, Eradication, and Recovery",
                "D": "Post-Incident Activity"
            },
            "answer": "D",
            "explanation": "Post-Incident Activity: Review lessons learned and improve."
        },
        {
            "topic": "Incident Response and Disaster Recovery",
            "question": "47. What is the Strategy and process of restoring critical business functions, data, and infrastructure after disruptions?",
            "options": {
                "A": "Incident Response",
                "B": "Security Auditing",
                "C": "Disaster Recovery",
                "D": "Risk Assessment"
            },
            "answer": "C",
            "explanation": "Disaster Recovery: Strategy and process of restoring critical business functions, data, and infrastructure after disruptions."
        },
        {
            "topic": "Incident Response and Disaster Recovery",
            "question": "48. Disaster Recovery ensures the organization can resume operations:",
            "options": {
                "A": "independently",
                "B": "efficiently",
                "C": "globally",
                "D": "automatically"
            },
            "answer": "B",
            "explanation": "Ensures the organization can resume operations efficiently."
        },
        {
            "topic": "Incident Response and Disaster Recovery",
            "question": "49. Which DR Step involves Identify threats and vulnerabilities?",
            "options": {
                "A": "Business Impact Analysis (BIA)",
                "B": "Strategy Development",
                "C": "Risk Assessment",
                "D": "Plan Development"
            },
            "answer": "C",
            "explanation": "Risk Assessment: Identify threats and vulnerabilities."
        },
        {
            "topic": "Incident Response and Disaster Recovery",
            "question": "50. Determining critical functions and systems is the purpose of which DR Step?",
            "options": {
                "A": "Risk Assessment",
                "B": "Plan Development",
                "C": "Business Impact Analysis (BIA)",
                "D": "Maintenance"
            },
            "answer": "C",
            "explanation": "Business Impact Analysis (BIA): Determine critical functions and systems."
        },
        {
            "topic": "Incident Response and Disaster Recovery",
            "question": "51. Which DR Step involves Define recovery methods for systems and data?",
            "options": {
                "A": "Business Impact Analysis (BIA)",
                "B": "Strategy Development",
                "C": "Testing",
                "D": "Maintenance"
            },
            "answer": "B",
            "explanation": "Strategy Development: Define recovery methods for systems and data."
        },
        {
            "topic": "Incident Response and Disaster Recovery",
            "question": "52. Document DR plan, roles, and procedures falls under which DR Step?",
            "options": {
                "A": "Plan Development",
                "B": "Strategy Development",
                "C": "Risk Assessment",
                "D": "Testing"
            },
            "answer": "A",
            "explanation": "Plan Development: Document DR plan, roles, and procedures."
        },
        {
            "topic": "Incident Response and Disaster Recovery",
            "question": "53. The DR Step that involves Regularly test DR plan effectiveness is:",
            "options": {
                "A": "Maintenance",
                "B": "Testing",
                "C": "Plan Development",
                "D": "Risk Assessment"
            },
            "answer": "B",
            "explanation": "Testing: Regularly test DR plan effectiveness."
        },
        {
            "topic": "Incident Response and Disaster Recovery",
            "question": "54. Review and update DR plan regularly is the focus of which DR Step?",
            "options": {
                "A": "Testing",
                "B": "Plan Development",
                "C": "Strategy Development",
                "D": "Maintenance"
            },
            "answer": "D",
            "explanation": "Maintenance: Review and update DR plan regularly."
        },
        {
            "topic": "Incident Response and Disaster Recovery",
            "question": "55. Which U.S. government agency develops standards, guidelines, and best practices for technology and cybersecurity, and publishes the SP 800-61 framework?",
            "options": {
                "A": "HIPAA",
                "B": "NIST",
                "C": "ISO/IEC 27001",
                "D": "GDPR"
            },
            "answer": "B",
            "explanation": "The National Institute of Standards and Technology (NIST) is a U.S. government agency that develops standards, guidelines, and best practices for technology and cybersecurity."
        },
        {
            "topic": "Incident Response and Disaster Recovery",
            "question": "56. Which of the following is an example of a cybersecurity incident mentioned in the text?",
            "options": {
                "A": "Natural disasters",
                "B": "Malware attacks",
                "C": "Power outages",
                "D": "System vulnerabilities"
            },
            "answer": "B",
            "explanation": "Examples [of Incident Response]: Malware attacks, Phishing attacks."
        },
        {
            "topic": "Incident Response and Disaster Recovery",
            "question": "57. Which of the following is an example of a disruption leading to Disaster Recovery procedures, mentioned in the text?",
            "options": {
                "A": "Phishing attacks",
                "B": "Malware attacks",
                "C": "Power outages",
                "D": "Ransomware Attack (2017)"
            },
            "answer": "C",
            "explanation": "Examples [of Disaster Recovery]: Natural disasters, power outages."
        },
        {
            "topic": "Incident Response and Disaster Recovery",
            "question": "58. The WannaCry Ransomware Attack occurred in which year?",
            "options": {
                "A": "1996",
                "B": "2003",
                "C": "2017",
                "D": "2005"
            },
            "answer": "C",
            "explanation": "WannaCry Ransomware Attack (2017): Infected over 200,000 computers in 150 countries..."
        },
        {
            "topic": "Incident Response and Disaster Recovery",
            "question": "59. The WannaCry Ransomware Attack showed the importance of strong incident response and:",
            "options": {
                "A": "software updates",
                "B": "Disaster Recovery",
                "C": "recovery plans",
                "D": "power outages"
            },
            "answer": "C",
            "explanation": "WannaCry... showed importance of software updates, strong incident response, and recovery plans."
        },
        {
            "topic": "Incident Response and Disaster Recovery",
            "question": "60. The NIST (SP 800-61) phases of Incident Response are used globally, not just in the U.S., because they’re practical and:",
            "options": {
                "A": "planned",
                "B": "detailed",
                "C": "tested",
                "D": "maintained"
            },
            "answer": "B",
            "explanation": "Their frameworks are used globally, not just in the U.S., because they’re practical and detailed."
        },

        # --- Topic 4: Security Auditing and Penetration Testing (Q61-Q80) ---
        {
            "topic": "Security Auditing and Penetration Testing",
            "question": "61. What is Checking a system or network to see if it is safe?",
            "options": {
                "A": "Penetration Testing",
                "B": "Reporting",
                "C": "Security Auditing",
                "D": "Gaining Access"
            },
            "answer": "C",
            "explanation": "Security Auditing: Checking a system or network to see if it is safe."
        },
        {
            "topic": "Security Auditing and Penetration Testing",
            "question": "62. The purpose of Security Auditing is to Find security problems before hackers do, ensure rules are followed, and:",
            "options": {
                "A": "keep data safe",
                "B": "Simulate an attack",
                "C": "Discover weak spots",
                "D": "Test strength of security"
            },
            "answer": "A",
            "explanation": "Purpose: Find security problems before hackers do, ensure rules are followed, and keep data safe."
        },
        {
            "topic": "Security Auditing and Penetration Testing",
            "question": "63. Which type of audit is Done by company’s own team?",
            "options": {
                "A": "External Audit",
                "B": "Compliance Audit",
                "C": "Internal Audit",
                "D": "Penetration Test"
            },
            "answer": "C",
            "explanation": "Internal Audit: Done by company’s own team."
        },
        {
            "topic": "Security Auditing and Penetration Testing",
            "question": "64. Which type of audit is Done by outside experts?",
            "options": {
                "A": "Internal Audit",
                "B": "External Audit",
                "C": "Compliance Audit",
                "D": "Security Auditing"
            },
            "answer": "B",
            "explanation": "External Audit: Done by outside experts."
        },
        {
            "topic": "Security Auditing and Penetration Testing",
            "question": "65. The type of audit that Checks if system follows legal or company rules is a:",
            "options": {
                "A": "Internal Audit",
                "B": "External Audit",
                "C": "Compliance Audit",
                "D": "Security Audit"
            },
            "answer": "C",
            "explanation": "Compliance Audit: Checks if system follows legal or company rules."
        },
        {
            "topic": "Security Auditing and Penetration Testing",
            "question": "66. What is Simulating an attack to find system weaknesses?",
            "options": {
                "A": "Security Auditing",
                "B": "Compliance Audit",
                "C": "Penetration Testing",
                "D": "Internal Audit"
            },
            "answer": "C",
            "explanation": "Penetration Testing: Simulating an attack to find system weaknesses."
        },
        {
            "topic": "Security Auditing and Penetration Testing",
            "question": "67. In Penetration Testing, the Tester acts like a hacker, but with:",
            "options": {
                "A": "a report",
                "B": "permission",
                "C": "weak spots",
                "D": "a system"
            },
            "answer": "B",
            "explanation": "Tester acts like a hacker, but with permission."
        },
        {
            "topic": "Security Auditing and Penetration Testing",
            "question": "68. One purpose of Penetration Testing is to Discover weak spots before:",
            "options": {
                "A": "external audits",
                "B": "real hackers do",
                "C": "reporting",
                "D": "scanning"
            },
            "answer": "B",
            "explanation": "Purpose: Discover weak spots before real hackers do, test strength of security, and improve defenses."
        },
        {
            "topic": "Security Auditing and Penetration Testing",
            "question": "69. Which step of Penetration Testing involves Decide what to test?",
            "options": {
                "A": "Scanning",
                "B": "Gaining Access",
                "C": "Planning",
                "D": "Reporting"
            },
            "answer": "C",
            "explanation": "Planning: Decide what to test."
        },
        {
            "topic": "Security Auditing and Penetration Testing",
            "question": "70. Which step of Penetration Testing involves Look for open ports or weak points?",
            "options": {
                "A": "Scanning",
                "B": "Gaining Access",
                "C": "Maintaining Access",
                "D": "Planning"
            },
            "answer": "A",
            "explanation": "Scanning: Look for open ports or weak points."
        },
        {
            "topic": "Security Auditing and Penetration Testing",
            "question": "71. The Penetration Testing step to Try to enter the system is:",
            "options": {
                "A": "Scanning",
                "B": "Gaining Access",
                "C": "Maintaining Access",
                "D": "Reporting"
            },
            "answer": "B",
            "explanation": "Gaining Access: Try to enter the system."
        },
        {
            "topic": "Security Auditing and Penetration Testing",
            "question": "72. Which Penetration Testing step involves See how long you can stay undetected?",
            "options": {
                "A": "Planning",
                "B": "Scanning",
                "C": "Gaining Access",
                "D": "Maintaining Access"
            },
            "answer": "D",
            "explanation": "Maintaining Access: See how long you can stay undetected."
        },
        {
            "topic": "Security Auditing and Penetration Testing",
            "question": "73. Share results and fixes describes which Penetration Testing step?",
            "options": {
                "A": "Gaining Access",
                "B": "Planning",
                "C": "Reporting",
                "D": "Maintaining Access"
            },
            "answer": "C",
            "explanation": "Reporting: Share results and fixes."
        },
        {
            "topic": "Security Auditing and Penetration Testing",
            "question": "74. Security Audit Reviews settings, policies, and:",
            "options": {
                "A": "a real attack",
                "B": "compliance",
                "C": "weak spots",
                "D": "fixes"
            },
            "answer": "B",
            "explanation": "Security Audit: Reviews settings, policies, and compliance."
        },
        {
            "topic": "Security Auditing and Penetration Testing",
            "question": "75. A Security Audit is considered Less:",
            "options": {
                "A": "active",
                "B": "risky",
                "C": "open",
                "D": "secure"
            },
            "answer": "B",
            "explanation": "Security Audit: Reviews settings, policies, and compliance. Less risky."
        },
        {
            "topic": "Security Auditing and Penetration Testing",
            "question": "76. Penetration Test Simulates a:",
            "options": {
                "A": "Compliance Audit",
                "B": "real attack",
                "C": "security setup",
                "D": "weak point"
            },
            "answer": "B",
            "explanation": "Penetration Test: Simulates a real attack."
        },
        {
            "topic": "Security Auditing and Penetration Testing",
            "question": "77. Penetration Test is described as More active and:",
            "options": {
                "A": "secure",
                "B": "compliant",
                "C": "risky",
                "D": "undetected"
            },
            "answer": "C",
            "explanation": "Penetration Test: Simulates a real attack. More active and risky."
        },
        {
            "topic": "Security Auditing and Penetration Testing",
            "question": "78. Audit is Checking locks; Pen test is Trying to:",
            "options": {
                "A": "fix the locks",
                "B": "check the keys",
                "C": "open the locks",
                "D": "share results"
            },
            "answer": "C",
            "explanation": "Audit = Checking locks; Pen test = Trying to open the locks."
        },
        {
            "topic": "Security Auditing and Penetration Testing",
            "question": "79. A benefit of both Security Auditing and Penetration Testing is to Find and fix problems:",
            "options": {
                "A": "later",
                "B": "early",
                "C": "passively",
                "D": "risky"
            },
            "answer": "B",
            "explanation": "Benefits of Both: Find and fix problems early."
        },
        {
            "topic": "Security Auditing and Penetration Testing",
            "question": "80. Security Auditing and Penetration Testing help to Protect company:",
            "options": {
                "A": "reputation",
                "B": "policies",
                "C": "settings",
                "D": "systems"
            },
            "answer": "A",
            "explanation": "Benefits of Both: Protect company reputation."
        }
    ]

    for i, q in enumerate(quiz):
        print("\n" + "="*50)
        print(f"Topic: {q['topic']} | Question {i + 1}/80")
        print("="*50)
        print(q['question'])
        for option, text in q['options'].items():
            print(f"  {option}. {text}")

        # Simulate user input and display answer
        input("\n[Press Enter to reveal the answer...]")
        print(f"\nCorrect Answer: {q['answer']}")
        # Optionally display the full extracted sentence (The explanation already covers this by design)
        # print(f"Source Text: {q['explanation']}")
        print("="*50)

    print("\n--- Quiz Finished ---")

if __name__ == "__main__":
    run_quiz()