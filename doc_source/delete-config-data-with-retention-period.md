# Deleting AWS Config Data<a name="delete-config-data-with-retention-period"></a>

AWS Config allows you to delete your data by specifying a retention period for your `ConfigurationItems`\. When you specify a retention period, AWS Config retains your `ConfigurationItems` for that specified period\. You can choose a period between a minimum of 30 days and a maximum of 7 years \(2557 days\)\. AWS Config deletes data older than your specified retention period\. If you do not specify a retention period, AWS Config continues to store `ConfigurationItems` for the default period of 7 years \(2557 days\)\. When recording is switched on, the current state of the resource is when a `ConfigurationItem` is recorded and until the next change \(a new `ConfigurationItem`\) is recorded\.

To understand the behavior of retention period, let's take a look at the timeline\.
+ When recording is switched on, the current state of a resource always exists and can't be deleted irrespective of the date the `ConfigurationItem` is recorded\.
+ When AWS Config records new `ConfigurationItems`, the previous `ConfigurationItems` are deleted depending on the specified retention period\.

In the following timeline, AWS Config records `ConfigurationItems` at the following dates\. For the purpose of this timeline, today is represented as May 24, 2018\.

![\[AWS Config retention period example\]](http://docs.aws.amazon.com/config/latest/developerguide/images/retention-period-timeline.png)

The following table explains which `ConfigurationItems` are displayed on the AWS Config timeline based on selected retention period\.


****  

| Retention Period | Configuration Items displayed on timeline | Explanation | 
| --- | --- | --- | 
| 30 days | December 12, 2017 | The current state of the resource started from December 12, 2017 when the `ConfigurationItem` was recorded and is valid until today \(May 24, 2018\)\. When recording is turned on, the current state always exists\. | 
| 365 days | December 12, 2017; November 12, 2017, and March 10, 2017 | The retention period shows the current state December 12, 2017 and previous `ConfigurationItems` November 12, 2017 and March 10, 2017\.  The `ConfigurationItem` for March 10, 2017 is displayed on the timeline because that configuration state represented the current state 365 days ago\.   | 

After you specify a retention period, AWS Config APIs no longer return `ConfigurationItems` that represent a state older than the specified retention period\. 

**Note**  
AWS Config cannot record your `ConfigurationItems` if recording is switched off\.
AWS Config cannot record your `ConfigurationItems` if your IAM role is broken\.

## Setting Data Retention Period in AWS Management Console<a name="delete-config-data-with-retention-period-console"></a>

In the AWS Management Console, if you do not select a data retention period, the default period is 7 years or 2557 days\.

To set a custom data retention period for configuration items select the checkbox\. You can select 1 year, 3 years, 5 years, or a custom period\. For a custom period, enter the number of days between 30 and 2557 days\.

![\[AWS Config retention period example\]](http://docs.aws.amazon.com/config/latest/developerguide/images/retention-period-console.png)