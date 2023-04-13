# s3\-event\-notifications\-enabled<a name="s3-event-notifications-enabled"></a>

Checks if Amazon S3 Events Notifications are enabled on an S3 bucket\. The rule is NON\_COMPLIANT if S3 Events Notifications are not set on a bucket, or if the event type or destination do not match the `eventTypes` and destinationArn parameters\. 

**Identifier:** S3\_EVENT\_NOTIFICATIONS\_ENABLED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), China \(Ningxia\) Region

**Parameters:**

destinationArn \(Optional\)Type: String  
The Amazon Resource Name \(ARN\) of the destination for the event notification \(Amazon SNS topic, AWS Lambda, Amazon SQS Queue\)\.

eventTypes \(Optional\)Type: CSV  
Comma\-separated list of the preferred Amazon S3 event types

## AWS CloudFormation template<a name="w2aac12c33c15b9d545c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.