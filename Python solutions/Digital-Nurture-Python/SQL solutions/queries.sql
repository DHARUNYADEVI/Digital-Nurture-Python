-- Query 1
select u.full_name,e.title,e.city,e.start_date
FROM users u
JOIN registrations r ON u.user_id=r.user_id
JOIN events e ON r.event_id=e.event_id
where status='upcoming'
AND u.city=e.city
order by e.start_date;

-- Query 2
select e.title, avg(f.rating) as avg_rating,count(*) as feedback_count
from events e
join feedback f on e.event_id=f.event_id
group by e.event_id,e.title
having count(*)>=10
order by avg_rating desc;

-- Query 3
select * from users
where user_id not in(
select distinct user_id 
from registrations
where registration_date>=(
select date_sub(max(registration_date),interval 90 day)
from registrations)
);

-- Query 4
select e.title,
count(s.session_id) as session_count
from events e
join sessions s on e.event_id=s.event_id
where time(s.start_time)between'10:00:00' and '12:00:00'
group by e.title;

-- Query 5
select u.city,
count(distinct r.registration_id) as registrations
from users u
join registrations r on u.user_id=r.user_id
group by u.city
order by registrations desc
limit 5;

-- Query 6
select e.title, r.resource_type, count(*) as total_resources
from events e
join resources r on e.event_id=r.event_id
group by e.title,r.resource_type;

-- Query 7
select u.full_name, e.title, f.rating, f.comments
from feedback f
join users u on f.user_id=u.user_id
join events e on f.event_id=e.event_id
where f.rating<3;

-- Query 8
select e.title,count(session_id)as total_sessions
from events e
left join sessions s on e.event_id=s.event_id
where e.status='upcoming'
group by e.title;

-- Query 9
select u.full_name,e.status,count(*) as total_events
from users u
join events e on u.user_id=e.organizer_id
group by u.full_name,e.status;

-- Query 10
select e.event_id,e.title
from events e
join registrations r on e.event_id=r.event_id
left join feedback f on e.event_id=f.event_id
where f.feedback_id is null;

-- Query 11
select registration_date,count(*)as new_users
from users
where registration_date>=(
select date_sub(max(registration_date),interval 7 day)
from users)
group by registration_date;

-- Query 12
select e.event_id,e.title,count(session_id)as total_sessions
from events e
join sessions s on e.event_id=s.event_id
group by e.event_id,e.title
having count(s.session_id)=(
select max(session_count)
from (
select count(*) session_count
from sessions
group by event_id) x
);

-- Query 13
select e.city,avg(f.rating)as avg_rating
from events e
join feedback f on e.event_id=f.event_id
group by e.city
order by e.city;

-- Query 14
select e.title,count(r.registration_id)registrations
from events e
join registrations r on e.event_id=r.event_id
group by e.title
order by registrations desc
limit 3;

-- Query 15
select s1.event_id,s1.title,s2.title
from sessions s1
join sessions s2 on s1.event_id=s2.event_id
and s1.session_id<s2.session_id
and s1.start_time<s2.end_time
and s1.end_time>s2.start_time;

-- Query 16
select * from users
where registration_date>=(
select date_sub(max(registration_date),interval 30 day)
from users )
and user_id not in(
select user_id
from registrations);

-- Query 17
select speaker_name,count(*) total_sessions
from sessions
group by speaker_name
having count(*)>1;

-- Query 18
select e.title
from events e
left join resources r on e.event_id=r.event_id
where r.resource_id is null;

-- Query 19
select e.event_id,e.title, count(distinct r.registration_id) as registrations,avg(f.rating) as avg_rating
from events e
left join registrations r on e.event_id=r.event_id
left join feedback f on e.event_id=f.event_id
where e.status='completed'
group by e.event_id,e.title;

-- Query 20
select u.user_id,u.full_name,count(distinct r.event_id)as events_attended,
count(distinct f.feedback_id) as feedbacks_Submitted
from users u
left join registrations r on u.user_id=r.user_id
left join feedback f on u.user_id=f.user_id
group by u.user_id,u.full_name
order by u.user_id;

-- Query 21
select u.user_id,u.full_name,
count(f.feedback_id) as feedback_count
from users u
join feedback f on u.user_id=f.user_id
group by u.user_id,u.full_name
order by feedback_count desc, u.user_id
limit 5;

-- Query 22
select user_id,event_id,count(*) as registration_count
from registrations
group by user_id,event_id
having count(*) > 1;

-- Query 23
select date_format(registration_date,'%Y-%m') as month,
count(*) registrations
from registrations
group by month
order by month;

-- Query 24
select e.title, round(avg(timestampdiff(minute,s.start_time,s.end_time)),2) avg_duration
from events e
join sessions s on e.event_id=s.event_id
group by e.title;

-- Query 25
select e.event_id,e.title
from events e
left join sessions s on e.event_id=s.event_id
where s.session_id is null
order by e.event_id;