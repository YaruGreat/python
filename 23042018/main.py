from VkAPI import VkAPI


def main():
    id1 = 88896669
    id2 = 393055
    q = VkAPI.my_frieds_get_mutual(id1, id2)
    VkAPI.user_info_by_id(q)

if __name__ == '__main__':
    main()
