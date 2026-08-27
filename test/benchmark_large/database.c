#include <stddef.h>
#include "database.h"
#include "config.h"

static User users[MAX_USERS];
static int user_count = 0;

void database_init(void) {
    user_count = 0;
}

int database_add_user(User *user) {
    if (user_count >= MAX_USERS) {
        return 0;
    }

    users[user_count] = *user;
    user_count++;

    return 1;
}

User *database_find_user(int id) {
    for (int i = 0; i < user_count; i++) {
        if (users[i].id == id) {
            return &users[i];
        }
    }

    return NULL;
}

int database_remove_user(int id) {
    User *user = database_find_user(id);

    if (user == NULL) {
        return 0;
    }

    user->active = 0;
    return 1;
}

int database_user_count(void) {
    return user_count;
}
