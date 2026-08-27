#ifndef AUTH_H
#define AUTH_H

#include "user.h"

int authenticate_user(const User *user);
int authorize_user(const User *user, const char *permission);

#endif

