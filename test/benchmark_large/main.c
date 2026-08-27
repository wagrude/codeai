#include <stdio.h>

#include "config.h"
#include "user.h"
#include "database.h"
#include "auth.h"
#include "logger.h"

int main(void) {
    database_init();

    User admin;
    User guest;

    init_user(&admin, 1, "admin");
    init_user(&guest, 2, "guest");

    database_add_user(&admin);
    database_add_user(&guest);

    User *user = database_find_user(1);

    if (user != NULL && authenticate_user(user)) {
        log_user_action(user->id, "authenticated");

        if (authorize_user(user, "admin")) {
            log_info("admin access granted");
        }
    }

    printf("Users: %d\n", database_user_count());

    deactivate_user(&guest);

    return 0;
}
