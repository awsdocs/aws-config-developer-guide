# Using Service\-Linked Roles for AWS Config<a name="using-service-linked-roles"></a>

AWS Config uses AWS Identity and Access Management \(IAM\)[ service\-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role)\. A service\-linked role is a unique type of IAM role that is linked directly to AWS Config\. Service\-linked roles are predefined by AWS Config and include all the permissions that the service requires to call other AWS services on your behalf\. 

A service\-linked role makes setting up AWS Config easier because you don’t have to manually add the necessary permissions\. AWS Config defines the permissions of its service\-linked roles, and unless defined otherwise, only AWS Config can assume its roles\. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity\.

For information about other services that support service\-linked roles, see [AWS Services That Work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes **in the **Service\-Linked Role** column\. Choose a **Yes** with a link to view the service\-linked role documentation for that service\.

## Service\-Linked Role Permissions for AWS Config<a name="slr-permissions"></a>

AWS Config uses the service\-linked role named **AWSServiceRoleForConfig** – AWS Config uses this service\-linked role to call other AWS services on your behalf\.

The **AWSServiceRoleForConfig** service\-linked role trusts the `config.amazonaws.com` service to assume the role\.

The permissions policy for the `AWSServiceRoleForConfig` role contains read\-only and write\-only permissions on the AWS Config resources and read\-only permissions for resources in other services that AWS Config supports\. For more information, see [Supported Resource Types](resource-config-reference.md)\. 

You must configure permissions to allow an IAM entity \(such as a user, group, or role\) to create, edit, or delete a service\-linked role\. For more information, see [Service\-Linked Role Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*\.

To use a service\-linked role with AWS Config, you must configure permissions on your Amazon S3 bucket and Amazon SNS topic\. For more information, see [Required Permissions for the Amazon S3 Bucket When Using Service\-Linked Roles](s3-bucket-policy.md#required-permissions-using-servicelinkedrole) and [Required Permissions for the Amazon SNS Topic When Using Service\-Linked Roles](sns-topic-policy.md#required-permissions-snstopic-using-servicelinkedrole)\. 

## Creating a Service\-Linked Role for AWS Config<a name="create-slr"></a>

In the IAM CLI or the IAM API, create a service\-linked role with the `config.amazonaws.com` service name\. For more information, see [Creating a Service\-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*\. If you delete this service\-linked role, you can use this same process to create the role again\.

## Editing a Service\-Linked Role for AWS Config<a name="edit-slr"></a>

AWS Config does not allow you to edit the **AWSServiceRoleForConfig** service\-linked role\. After you create a service\-linked role, you cannot change the name of the role because various entities might reference the role\. However, you can edit the description of the role using IAM\. For more information, see [Editing a Service\-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*\.

## Deleting a Service\-Linked Role for AWS Config<a name="delete-slr"></a>

If you no longer need to use a feature or service that requires a service\-linked role, we recommend that you delete that role\. That way you don’t have an unused entity that is not actively monitored or maintained\. However, you must clean up the resources for your service\-linked role before you can manually delete it\. 

**Note**  
If the AWS Config service is using the role when you try to delete the resources, then the deletion might fail\. If that happens, wait for a few minutes and try the operation again\.

**To delete AWS Config resources used by the **AWSServiceRoleForConfig****

Ensure that you do not have `ConfigurationRecorders` using the service\-linked role\. You can use the AWS Config console to stop the configuration recorder\. To stop recording, under **Recording is on**, choose **Turn off**\.

You can delete the `ConfigurationRecorder` using AWS Config API\. To delete, use the `delete-configuration-recorder` command\.

```
        $ aws configservice delete-configuration-recorder --configuration-recorder-name default
```

**To manually delete the service\-linked role using IAM**

Use the IAM console, the IAM CLI, or the IAM API to delete the AWSServiceRoleForConfig service\-linked role\. For more information, see [Deleting a Service\-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*\.