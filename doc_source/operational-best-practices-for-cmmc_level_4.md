# Operational Best Practices for CMMC Level 4<a name="operational-best-practices-for-cmmc_level_4"></a>

Conformance packs provide a general\-purpose compliance framework designed to enable you to create security, operational or cost\-optimization governance checks using managed or custom AWS Config rules and AWS Config remediation actions\. Conformance Packs, as sample templates, are not designed to fully ensure compliance with a specific governance or compliance standard\. You are responsible for making your own assessment of whether your use of the Services meets applicable legal and regulatory requirements\.

The following provides a sample mapping between the Cybersecurity Maturity Model Certification \(CMMC\) Level 4 and AWS managed Config rules\. Each Config rule applies to a specific AWS resource, and relates to one or more CMMC Level 4 controls\. A CMMC Level 4 control can be related to multiple Config rules\. Refer to the table below for more detail and guidance related to these mappings\.

**AWS Region:** All AWS Regions where conformance packs are supported \([Region support](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html#conformance-packs-regions)\) except AWS GovCloud \(US\-East\) and AWS GovCloud \(US\-West\)

**Note**  
Due to tentative guidance provided by the DoD and the CMMC Accreditation Body with respect to FedRAMP reciprocity for CMMC Level 3 \- 5, it is recommended that customers use AWS GovCloud \(US\) regions at this time for any workloads that require compliance with CMMC Level 3 \- 5\. As such, conformance pack templates for CMMC Levels 3 \- 5 are not available within the conformance pack console to avoid confusion\. Customers may independently install Config rules that map the tentative guidance for CMMC Level 3\-5 \(without a conformance pack template\) via CloudFormation using the sample YAML file linked within this document\.


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/operational-best-practices-for-cmmc_level_4.html)

## Template<a name="cmmc_level_4-conformance-pack-sample"></a>

The template is available on GitHub: [Operational Best Practices for CMMC Level 4](https://github.com/awslabs/aws-config-rules/blob/master/aws-config-conformance-packs/Operational-Best-Practices-for-CMMC-Level-4.yaml)\.