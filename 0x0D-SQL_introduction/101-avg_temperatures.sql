-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY City ORDER BY avg_temp DESC;
