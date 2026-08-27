#include <stdio.h>
#include "logger.h"

void log_info(const char *message) {
    printf("[INFO] %s\n", message);
}

void log_error(const char *message) {
    printf("[ERROR] %s\n", message);
}

void log_user_action(int user_id, const char *action) {
    printf("[USER %d] %s\n", user_id, action);
}
