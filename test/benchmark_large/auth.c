#include <string.h>
#include "auth.h"

int authenticate_user(const User *user) {
    if (user == NULL) {
        return 0;
    }

    return user->active;
}

int authorize_user(const User *user, const char *permission) {
    if (!authenticate_user(user)) {
        return 0;
    }

    if (strcmp(permission, "admin") == 0) {
        return user->id == 1;
    }

    return 1;
}
