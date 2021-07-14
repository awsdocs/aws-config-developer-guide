# Turning on AWS Config<a name="gs-cli-subscribe"></a>

You can use the AWS CLI to turn on AWS Config with the [put\-configuration\-recorder](https://docs.aws.amazon.com/cli/latest/reference/configservice/put-configuration-recorder.html) and [put\-delivery\-channel](https://docs.aws.amazon.com/cli/latest/reference/configservice/put-delivery-channel.html) commands and a few parameters\.

You can use the `put-configuration-recorder` command to create a new configuration recorder to record selected resource configurations\. The `put-delivery-channel` command creates a delivery channel object to deliver configuration information to an Amazon S3 bucket and Amazon SNS topic\. You can have one configuration recorder and one delivery channel per region in your account\.

You can specify the name of the recorder and the Amazon Resource Name \(ARN\) of the IAM role used to describe the AWS resources associated with the account\. By default, AWS Config automatically assigns the name "default" when creating the configuration recorder\. You cannot change the assigned name\. The `put-configuration-recorder` command uses the following options for the `--recording-group` parameter:
+ `allSupported=true` – AWS Config records configuration changes for every supported type of *regional resource*\. When AWS Config adds support for a new type of regional resource, it automatically starts recording resources of that type\.
+ `includeGlobalResourceTypes=true` – AWS Config includes supported types of global resources with the resources that it records\. When AWS Config adds support for a new type of global resource, it automatically starts recording resources of that type\.

  Before you can set this option to `true`, you must set the `allSupported` option to `true`\.

  If you do not want to include global resources, set this option to `false`, or omit it\.

Your command should look like the following example:

```
$ aws configservice put-configuration-recorder --configuration-recorder name=default,roleARN=arn:aws:iam::123456789012:role/config-role --recording-group allSupported=true,includeGlobalResourceTypes=true
```

To setup the delivery channel, use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/put-delivery-channel.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/put-delivery-channel.html) command:

```
$ aws configservice put-delivery-channel --delivery-channel file://deliveryChannel.json
```

The deliveryChannel\.json file specifies the delivery channel attributes:

```
{
    "name": "default",
    "s3BucketName": "config-bucket-123456789012",
    "snsTopicARN": "arn:aws:sns:us-east-2:123456789012:config-topic",
    "configSnapshotDeliveryProperties": {
        "deliveryFrequency": "Twelve_Hours"
    }
}
```

This example sets the following attributes:
+ `name` – The name of the delivery channel\. By default, AWS Config assigns the name `default` to a new delivery channel\.

  You cannot update the delivery channel name with the `put-delivery-channel` command\. For the steps to change the name, see [Renaming the Delivery Channel](manage-delivery-channel.md#update-dc-rename)\.
+ `s3BucketName` – The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files\.

  If you specify a bucket that belongs to another AWS account, that bucket must have policies that grant access permissions to AWS Config\. For more information, see [Permissions for the Amazon S3 Bucket](s3-bucket-policy.md)\.
+ `snsTopicARN` – The Amazon Resource Name \(ARN\) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes\.

  If you choose a topic from another account, that topic must have policies that grant access permissions to AWS Config\. For more information, see [Permissions for the Amazon SNS Topic](sns-topic-policy.md)\.
+ `configSnapshotDeliveryProperties` – Contains the `deliveryFrequency` attribute, which sets how often AWS Config delivers configuration snapshots\.