# Query Components<a name="query-components"></a>

The SQL `SELECT` query components are as follows\.

## Synopsis<a name="synopsis"></a>

```
SELECT property [, ...]
[ WHERE condition ]
[ GROUP BY property ]
[ ORDER BY property [ ASC | DESC ] [, property [ ASC | DESC ] ...] ]
```

## Parameters<a name="parameters"></a>

**\[ WHERE condition \]**  
Filters results according to the `condition` you specify\.

**\[ GROUP BY property \]**  
Aggregates the result set into groups of rows with matching values for the given property\.  
The GROUP BY clause is applicable to aggregations\. AWS Config supports grouping by only one property\. 

**\[ ORDER BY property \[ ASC \| DESC \] \[, property \[ ASC \| DESC \] \.\.\.\] \]**  
Sorts a result set by one or more output `properties`\.  
When the clause contains multiple properties, the result set is sorted according to the first `property`, then according to the second `property` for rows that have matching values for the first property, and so on\. 

## Examples<a name="examples"></a>

```
SELECT resourceId WHERE resourceType='AWS::EC2::Instance'
```

```
SELECT configuration.complianceType, COUNT(*) WHERE resourceType = 'AWS::Config::ResourceCompliance' GROUP BY configuration.complianceType  
```