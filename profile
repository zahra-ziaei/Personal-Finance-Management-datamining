select * from hadaf_user

select count(first_name) fname, count(last_name) lname,  count (national_id) meli,
count(birth_date) birth, count(gender) gender, count(education) education, count(is_married) married,
count (children) child, count(home_town) town, count (email_address) email
from hadaf_user



select count(*)
from hadaf_user
where children is not null
and is_married is not null


select count(*)
from hadaf_user
where children is not null
or is_married is not null
