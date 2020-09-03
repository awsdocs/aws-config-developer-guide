# Verify that AWS Config Is On<a name="gs-cli-verify-subscribe"></a>

Once you have turned on AWS Config, you can use AWS CLI commands to verify that the AWS Config is running and that the `subscribe` command has created a configuration recorder and a delivery channel\. You can also confirm that AWS Config has started recording and delivering configurations to the delivery channel\.

**Contents**
+ [Verify that the Delivery Channel Is Created](#gs-cli-verify-channel)
+ [Verify that the Configuration Recorder Is Created](#gs-cli-verify-recorder)
+ [Verify that AWS Config has started recording](#gs-cli-verify-config-recording)

## Verify that the Delivery Channel Is Created<a name="gs-cli-verify-channel"></a>

Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-delivery-channels.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-delivery-channels.html) command to verify that your Amazon S3 bucket and Amazon SNS topic is configured\.

```
$ aws configservice describe-delivery-channels
{
    "DeliveryChannels": [
        {
            "snsTopicARN": "arn:aws:sns:us-west-2:0123456789012:my-config-topic",
            "name": "my-delivery-channel",
            "s3BucketName": "my-config-bucket"
        }
    ]
}
```

When you use the CLI, the service API, or the SDKs to configure your delivery channel and do not specify a name, AWS Config automatically assigns the name "`default`"\. 

## Verify that the Configuration Recorder Is Created<a name="gs-cli-verify-recorder"></a>

Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-configuration-recorders.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-configuration-recorders.html) command to verify that a configuration recorder is created and that the configuration recorder has assumed an IAM role\. For more information, see [Creating an IAM Role](gs-cli-prereq.md#gs-cli-create-iamrole)\.

```
$ aws configservice describe-configuration-recorders
{
    "ConfigurationRecorders": [
        {
            "roleARN": "arn:aws:iam::012345678912:role/myConfigRole",
            "name": "default"
        }
    ]
}
```

## Verify that AWS Config has started recording<a name="gs-cli-verify-config-recording"></a>

Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-configuration-recorder-status.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-configuration-recorder-status.html) command to verify that the AWS Config has started recording the configurations of the supported AWS resources existing in your account\. The recorded configurations are delivered to the specified delivery channel\.

```
$ aws configservice describe-configuration-recorder-status
{
    "ConfigurationRecordersStatus": [
        {
            "name": "default",
            "lastStatus": "SUCCESS",
            "lastStopTime": 1414511624.914,
            "lastStartTime": 1414708460.276,
            "recording": true,
            "lastStatusChangeTime": 1414816537.148,
            "lastErrorMessage": "NA",
            "lastErrorCode": "400"
        }
    ]
}
```

The value `true` in the `recording` field confirms that the configuration recorder has started recording configurations of all your resources\. AWS Config records the time in UTC\. The output is displayed as a Unix timestamp\.  

For information about looking up the resources existing in your account and understanding the configurations of your resources, see [Viewing AWS Resource Configurations and History](view-manage-resource.md)\.