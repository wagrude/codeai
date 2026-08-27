#include <string.h>
#include "user.h"

void init_user(User *user, int id, const char *name) {
    user->id = id;
    strncpy(user->name, name, 63);
    user->name[63] = '\0';
    user->active = 1;
}

void deactivate_user(User *user) {
    user->active = 0;
}

int is_user_active(const User *user) {
    return user->active;
}
