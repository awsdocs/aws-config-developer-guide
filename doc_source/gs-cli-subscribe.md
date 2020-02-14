# Turning on AWS Config<a name="gs-cli-subscribe"></a>

You can use the AWS CLI to turn on AWS Config with the [subscribe](https://docs.aws.amazon.com/cli/latest/reference/configservice/subscribe.html) command and a few parameters\.

You can use the `subscribe` command to have AWS Config start recording configurations of all supported AWS resources in your account\. The `subscribe` command creates a configuration recorder, a delivery channel using a specified Amazon S3 bucket and Amazon SNS topic, and starts recording the configuration items\. You can have one configuration recorder and one delivery channel per region in your account\.

To turn on AWS Config, use the `subscribe` with the following parameters:

The `subscribe` command uses the following options:

`--s3-bucket`  
Specify the name of an Amazon S3 bucket existing in your account or existing in another account\.

`--sns-topic`  
Specify the Amazon Resource Name \(ARN\) of an SNS topic existing in your account or existing in another account\.

`--iam-role`  
Specify the Amazon Resource Name \(ARN\) of an existing IAM Role\.  
The specified IAM role must have policies attached that grant AWS Config permissions to deliver configuration items to the Amazon S3 bucket and the Amazon SNS topic, and the role must grant permissions to the `Describe` APIs of the supported AWS resources\.

Your command should look like the following example:

```
$ aws configservice subscribe --s3-bucket my-config-bucket --sns-topic arn:aws:sns:us-east-2:012345678912:my-config-notice --iam-role arn:aws:iam::012345678912:role/myConfigRole
```

After you run the `subscribe` command, AWS Config records all supported resources that it finds in the region\. If you don't want AWS Config to record supported resources, specify the types of resources to record by updating the configuration recorder to use a recording group\. For more information, see [Selecting Resources \(AWS CLI\)](select-resources.md#select-resources-cli)\.