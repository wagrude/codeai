#ifndef USER_H
#define USER_H

typedef struct {
    int id;
    char name[64];
    int active;
} User;

void init_user(User *user, int id, const char *name);
void deactivate_user(User *user);
int is_user_active(const User *user);

#endif
