# Example Oversized Configuration Item Change Notification<a name="oversized-notification-example"></a>

When AWS Config detects a configuration change for a resource, it sends a configuration item notification\. If the notification exceeds the maximum size allowed by Amazon Simple Notification Service \(Amazon SNS\), the notification includes a brief summary of the configuration item\. You can view the complete notification in the Amazon S3 bucket location specified in the `s3BucketLocation` field\.

The following example notification shows a configuration item for an Amazon EC2 instance\. The notification includes a summary of the changes and the location of the notification in the Amazon S3 bucket\. 

```
View the Timeline for this Resource in AWS Config Management Console:
    https://console.aws.amazon.com/config/home?region=us-west-2#/timeline/AWS::EC2::Instance/resourceId_14b76876-7969-4097-ab8e-a31942b02e80?time=2016-10-06T16:46:16.261Z
    
    The full configuration item change notification for this resource exceeded the maximum size allowed by Amazon Simple Notification Service (SNS). A summary of the configuration item is provided here. You can view the complete notification in the specified Amazon S3 bucket location.
    
    New State Record Summary:
    ----------------------------
    {
      "configurationItemSummary": {
        "changeType": "UPDATE",
        "configurationItemVersion": "1.2",
        "configurationItemCaptureTime": "2016-10-06T16:46:16.261Z",
        "configurationStateId": 0,
        "awsAccountId": "123456789012",
        "configurationItemStatus": "OK",
        "resourceType": "AWS::EC2::Instance",
        "resourceId": "resourceId_14b76876-7969-4097-ab8e-a31942b02e80",
        "resourceName": null,
        "ARN": "arn:aws:ec2:us-west-2:123456789012:instance/resourceId_14b76876-7969-4097-ab8e-a31942b02e80",
        "awsRegion": "us-west-2",
        "availabilityZone": null,
        "configurationStateMd5Hash": "8f1ee69b287895a0f8bc5753eca68e96",
        "resourceCreationTime": "2016-10-06T16:46:10.489Z"
      },
      "s3DeliverySummary": {
        "s3BucketLocation": "my-bucket/AWSLogs/123456789012/Config/us-west-2/2016/10/6/OversizedChangeNotification/AWS::EC2::Instance/resourceId_14b76876-7969-4097-ab8e-a31942b02e80/123456789012_Config_us-west-2_ChangeNotification_AWS::EC2::Instance_resourceId_14b76876-7969-4097-ab8e-a31942b02e80_20161006T164616Z_0.json.gz",
        "errorCode": null,
        "errorMessage": null
      },
      "notificationCreationTime": "2016-10-06T16:46:16.261Z",
      "messageType": "OversizedConfigurationItemChangeNotification",
      "recordVersion": "1.0"
    }
```