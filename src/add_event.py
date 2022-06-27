# CREATE TABLE IF NOT EXISTS task_list (
#                 task_id        integer     PRIMARY KEY AUTOINCREMENT,
#                 task_name      text        NOT NULL,
#                 weeks_days_id  integer,              -- If the event is repeating
#                 task_date      datetime,             -- one time a year event, ex. birthday
#                 user_id        integer,

#                 FOREIGN KEY (user_id)
#                     REFERENCES user (user_id)
#             );


#             CREATE TABLE IF NOT EXISTS weeks_days (
#                 weeks_days_id  integer PRIMARY KEY AUTOINCREMENT,
#                 task_id        integer,
#                 week_nr        integer,
#                 mon            integer,
#                 tue            integer,
#                 wed            integer,
#                 thu            integer,
#                 fri            integer,
#                 sat            integer,
#                 sun            integer,
#                 days_completed integer,

#                 FOREIGN KEY (task_id)
#                     REFERENCES task_list (task_id)
#             );