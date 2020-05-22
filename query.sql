

select
avg(lengh_cm)
from
petal;



select Vid_irisa.spicies_name, sepal.flower_id, sepal.width_cm from sepal
LEFT join Vid_irisa on sepal.species_id=Vid_irisa.species_id 
where sepal.width_cm > (select
avg(width_cm)
from
sepal)
order by  width_cm;


select  sepal.lengh_cm,  count(width_cm) from sepal
group by sepal.lengh_cm
order by sepal.lengh_cm;




