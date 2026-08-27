#ifndef LOGGER_H
#define LOGGER_H

void log_info(const char *message);
void log_error(const char *message);
void log_user_action(int user_id, const char *action);

#endif
