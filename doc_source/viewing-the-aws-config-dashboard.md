# Viewing the AWS Config Dashboard<a name="viewing-the-aws-config-dashboard"></a>

Use the **Dashboard** to see an overview of your resources, rules, and their compliance state\. This page helps you quickly identify the top resources in your account, and if you have any rules or resources that are noncompliant\. 

After setup, AWS Config starts recording the specified resources and then evaluates them against your rules\. It may take a few minutes for AWS Config to display your resources, rules, and their compliance states on the **Dashboard**\.

**To use the AWS Config Dashboard**

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. Choose **Dashboard**\.

1. Use the **Dashboard** to see an overview of your resources, rules, and their compliance state\.  
![\[The AWS Config Dashboard page shows you the number of resources and noncompliant rules that you have in your account.\]](http://docs.aws.amazon.com/config/latest/developerguide/images/AWS-Config-Dashboard-20.png)

   On the **Dashboard**, you can do the following:

   1. View the total number of resources that AWS Config is recording\.

   1. View the resource types that AWS Config is recording, in descending order \(the number of resources\)\. Choose a resource type to go to the **Resources inventory** page\.

   1. Choose **View all resources** to go to the **Resources inventory** page\.

   1. View the number of noncompliant rules\.

   1. View the number of noncompliant resources\.

   1. View the top noncompliant rules, in descending order \(the number of resources\)\.

   1. Choose **View all noncompliant rules** to go to the **Rules** page\.

The **Dashboard** shows the resources and rules specific to your region and account\. It does not show resources or rules from other regions or other AWS accounts\. 

**Note**  
The **Evaluate your AWS resource configuration using Config rules** message can appear on the **Dashboard** for the following reasons:  
You haven't set up AWS Config Rules for your account\. You can choose **Add rule** to go to the **Rules** page\.
AWS Config is still evaluating your resources against your rules\. You can refresh the page to see the latest evaluation results\.
 AWS Config evaluated your resources against your rules and did not find any resources in scope\. You can specify the resources for AWS Config to record in the **Settings** page\. For more information, see [Selecting Which Resources AWS Config Records](select-resources.md)\.