drop table if exists posts;
create table posts (
  id integer primary key autoincrement,
  user_id integer,
  post text not null,
  foreign key (user_id) references users(id)
);

drop table if exists users;
create table users (
  id integer primary key autoincrement,
  username text not null,
  password text not null
);
