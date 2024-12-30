from globals import theme_sim, function_sim, environment_sim, difficulty_sim, w_t, w_f, w_e, w_d

def compatibility(room_u, room_v):
    return (
        w_t * theme_sim[room_u.theme_tag][room_v.theme_tag] +
        w_f * function_sim[room_u.function_tag][room_v.function_tag] +
        w_e * environment_sim[room_u.environment_tag][room_v.environment_tag] +
        w_d * difficulty_sim[room_u.difficulty_tag][room_v.difficulty_tag]
    )
