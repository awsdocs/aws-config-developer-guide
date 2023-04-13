# Service Limits<a name="configlimits"></a>

The following table describes limits within AWS Config\. Unless noted otherwise, the quotas can be increased upon request\. You can [request a quota increase](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-config-service)\.

For information about other limits in AWS, see [AWS Service Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)\. 


**AWS Config Service Limits**  

| Description | Limit Value | Can be increased | 
| --- | --- | --- | 
| Maximum number of AWS Config Rules per Region per account | 400 | Yes | 
| Maximum number of configuration aggregators | 50 | Yes | 
| Maximum number of accounts in an aggregator | 10000 | No | 
| Maximum number of accounts added or deleted per week for all aggregators | 1000 | Yes | 
| Maximum number of Tags | 50 | No | 
| Maximum number of saved queries in a single account and a Region | 300 | Yes | 


**Single Account Conformance Packs**  

| Description | Limit Value | Can be increased | 
| --- | --- | --- | 
| Maximum number of conformance packs per account | 50 | No | 
| Maximum number of AWS Config Rules per conformance pack | 130 | No | 
| Maximum number of AWS Config Rules per Region per account across all conformance packs | 150 | No | 

**Note**  
AWS Config rules in conformance packs count in the limit for the Maximum number of AWS Config Rules per Region per account\.


**Organization Conformance Packs**  

| Description | Limit Value | Can be increased | 
| --- | --- | --- | 
| Maximum number of conformance packs per organization | 50 | No | 
| Maximum number of AWS Config Rules per organization conformance pack | 130 | No | 
| Maximum number of AWS Config Rules per Region per account across all organization conformance packs | 350 | No | 

**Note**  
Deploying at the organization level counts in the limit for child accounts\. AWS Config rules in conformance packs count in the limit for the Maximum number of AWS Config Rules per Region per account\.


**Organization Config Rules**  

| Description | Limit Value | Can be increased | 
| --- | --- | --- | 
| Maximum number of organization AWS Config rules per organization | 150 | No | 

**Note**  
Deploying at the organization level counts in the limit for child accounts\.