#ifndef DATABASE_H
#define DATABASE_H

#include "user.h"

void database_init(void);
int database_add_user(User *user);
User *database_find_user(int id);
int database_remove_user(int id);
int database_user_count(void);

#endif
