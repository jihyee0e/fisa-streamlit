import streamlit as st

# text를 입력하는 검색창 하나 생성
# ani_test 있는 글자가 일부라도 들어가면
# img_list 해당 그림 출력되는 검색창 만들기

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

search_ = st.text_input('검색하실 애니메이션을 입력하세요. ')

for ani in ani_list:
    if search_ in ani:
        img_idx = ani_list.index(ani)

if search_ != '':  # 초기상태를 이미지없이 실행
    st.image(img_list[img_idx])


# for i in range(len(search_)):
#     if search_[i] in ani_list[0]:
#         st.image(img_list[0])
#         st.logo(img_list[0])
#         break
#     elif search_[i] in ani_list[1]:
#         st.image(img_list[1])
#         st.logo(img_list[1])
#         break
#     elif search_[i] in ani_list[2]:
#         st.image(img_list[2])
#         st.logo(img_list[2])
#         break
#     else:
#         st.text('없어요.')