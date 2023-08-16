1a. 406
SELECT COUNT(DISTINCT species) AS Number_of_Tiger_Types FROM taxonomy WHERE species LIKE '%Tiger%';

1b. 9695
SELECT ncbi_id FROM taxonomy WHERE species LIKE '%Panthera tigris sumatrae%';
