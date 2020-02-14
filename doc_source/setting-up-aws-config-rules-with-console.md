# Setting Up AWS Config Rules with the Console<a name="setting-up-aws-config-rules-with-console"></a>

The **Rules** page provides initial AWS managed rules that you can add to your account\. After set up, AWS Config evaluates your AWS resources against the rules that you choose\. You can update the rules and create additional managed rules after set up\. 

To see the complete list of AWS managed rules, see [List of AWS Config Managed Rules](managed-rules-by-aws-config.md)\.

For example, you can choose the **cloudtrail\-enabled** rule, which evaluates whether your account has a CloudTrail trail\. If your account doesn't have a trail, AWS Config flags the resource type and the rule as noncompliant\.

![\[The AWS Config rules page shows how to add rules to your account for the first time.\]](http://docs.aws.amazon.com/config/latest/developerguide/)![\[The AWS Config rules page shows how to add rules to your account for the first time.\]](http://docs.aws.amazon.com/config/latest/developerguide/)![\[The AWS Config rules page shows how to add rules to your account for the first time.\]](http://docs.aws.amazon.com/config/latest/developerguide/)

On the **Rules** page, you can do the following:

1. Type in the search field to filter results by rule name, description, or label\. For example, type **EC2** to return rules that evaluate EC2 resource types or type **periodic** to return rules that have a periodic trigger\. Type "new" to search for newly added rules\. For more information about trigger types, see [Specifying Triggers for AWS Config Rules](evaluate-config-rules.md)\.

1. Choose **Select all** to add all rules or **Clear all** to remove all rules\.

1. Choose the arrow icon to see the next page of rules\.

1. Recently added rules are marked as **New**\.

1. See the labels to identify the service that the rule evaluates and if the rule has a periodic trigger\.

**To set up AWS Config rules**

1. On the **Rules** page, choose the rules that you want\. You can customize these rules and add other rules to your account after set up\.

1. Choose **Next**\.

1. On the **Review** page, verify your setup details, and then choose **Confirm**\.

   The **Rules** page shows your rules and their current compliance results in the table\. The result for each rule is **Evaluating\.\.\.** until AWS Config finishes evaluating your resources against the rule\. You can update the results with the refresh button\. When AWS Config finishes evaluations, you can see the rules and resource types that are compliant or noncompliant\. For more information, see [Viewing Configuration Compliance](evaluate-config_view-compliance.md)\.

**Note**  
AWS Config evaluates only the resource types that it is recording\. For example, if you add the **cloudtrail\-enabled** rule but don't record the CloudTrail trail resource type, AWS Config can't evaluate whether the trails in your account are compliant or noncompliant\. For more information, see [Selecting Which Resources AWS Config Records](select-resources.md)\.

You can view, edit, and delete your existing rules\. You can also create additional AWS managed rules or create your own\. For more information, see [Managing your AWS Config Rules](evaluate-config_manage-rules.md)\.