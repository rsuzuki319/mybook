create table message(
id serial primary key,
channel integer not null,
source text not null,
cotent text not null


)

create or replace function notify_on_insert() returns trigger as $$
begin
perform pg_notify(
'channel_' || new.channel,
cast (row_to_json(new) as text));
return null;
end;
$$ language plpgsql;

create trigger notify_on_message_inesert after insert on message
for each row execute procedure notify_on_insert();
