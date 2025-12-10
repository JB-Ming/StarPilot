import streamlit as st
import random
import time
from collections import deque

# 頁面配置
st.set_page_config(
    page_title="🐍 貪食蛇遊戲",
    page_icon="🐍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 自定義 CSS
st.markdown("""
    <style>
        .main {
            max-width: 600px;
            margin: 0 auto;
        }
        .game-info {
            display: flex;
            justify-content: space-around;
            margin: 20px 0;
        }
        .score-box {
            text-align: center;
            padding: 10px 20px;
            background-color: #f0f0f0;
            border-radius: 8px;
            flex: 1;
            margin: 0 10px;
        }
    </style>
""", unsafe_allow_html=True)

# 遊戲常數
GRID_SIZE = 20
CANVAS_SIZE = 400
CELL_SIZE = CANVAS_SIZE / GRID_SIZE

# 初始化遊戲狀態


def init_game_state():
    return {
        'snake': deque([(10, 10)]),
        'foods': set(),
        'direction': (1, 0),
        'next_direction': (1, 0),
        'score': 0,
        'game_running': False,
        'game_over': False,
        'level': 1
    }


# 初始化 session state
if 'game_state' not in st.session_state:
    st.session_state.game_state = init_game_state()
    st.session_state.high_score = 0

# 標題
st.title("🐍 貪食蛇遊戲")

# 遊戲資訊
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("分數", st.session_state.game_state['score'])
with col2:
    st.metric("最高分", st.session_state.high_score)
with col3:
    st.metric("難度", st.session_state.game_state['level'])

# 生成食物


def generate_food(state):
    while len(state['foods']) < 10:
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        pos = (x, y)

        if pos not in state['snake'] and pos not in state['foods']:
            food_type = 'green' if random.random() > 0.5 else 'red'
            state['foods'].add((pos, food_type))

# 更新遊戲狀態


def update_game(state):
    if not state['game_running'] or state['game_over']:
        return

    # 更新蛇的方向
    state['direction'] = state['next_direction']

    # 計算新頭部位置
    head_x, head_y = state['snake'][0]
    dx, dy = state['direction']
    new_head = (head_x + dx, head_y + dy)

    # 檢查牆壁碰撞
    if new_head[0] < 0 or new_head[0] >= GRID_SIZE or new_head[1] < 0 or new_head[1] >= GRID_SIZE:
        state['game_over'] = True
        state['game_running'] = False
        if state['score'] > st.session_state.high_score:
            st.session_state.high_score = state['score']
        return

    # 檢查自身碰撞
    if new_head in state['snake']:
        state['game_over'] = True
        state['game_running'] = False
        if state['score'] > st.session_state.high_score:
            st.session_state.high_score = state['score']
        return

    state['snake'].appendleft(new_head)

    # 檢查食物碰撞
    food_eaten = False
    for food_pos, food_type in list(state['foods']):
        if new_head == food_pos:
            state['score'] += 10
            state['foods'].discard((food_pos, food_type))
            food_eaten = True

            if food_type == 'red':
                # 紅點：蛇變短
                if len(state['snake']) > 1:
                    state['snake'].pop()
                if len(state['snake']) > 1:
                    state['snake'].pop()
            # 綠點：蛇變長（預設行為）

            # 更新難度
            new_level = state['score'] // 100 + 1
            if new_level != state['level']:
                state['level'] = new_level

            break

    if not food_eaten:
        state['snake'].pop()

    generate_food(state)

# 繪製遊戲板


def draw_game_board(state):
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches

    fig, ax = plt.subplots(1, 1, figsize=(6, 6))

    # 設定背景
    ax.set_xlim(-0.5, GRID_SIZE - 0.5)
    ax.set_ylim(-0.5, GRID_SIZE - 0.5)
    ax.set_aspect('equal')
    ax.invert_yaxis()
    ax.set_facecolor('#1a1a1a')

    # 繪製網格
    for i in range(GRID_SIZE + 1):
        ax.axhline(y=i - 0.5, color='#222222', linewidth=0.5)
        ax.axvline(x=i - 0.5, color='#222222', linewidth=0.5)

    # 繪製蛇
    for i, (x, y) in enumerate(state['snake']):
        if i == 0:
            # 蛇頭
            circle = patches.Circle(
                (x, y), 0.4, color='#00ff88', ec='#00ff41', linewidth=2)
            ax.add_patch(circle)
        else:
            # 蛇身
            rect = patches.Rectangle((x - 0.4, y - 0.4), 0.8, 0.8,
                                     linewidth=0, facecolor='#00ff41', alpha=0.8)
            ax.add_patch(rect)

    # 繪製食物
    for (x, y), food_type in state['foods']:
        if food_type == 'green':
            color = '#00ff00'
        else:
            color = '#ff0000'
        circle = patches.Circle((x, y), 0.35, color=color)
        ax.add_patch(circle)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    st.pyplot(fig, use_container_width=True)


# 遊戲控制區域
st.markdown("### 📋 遊戲控制")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("▶️ 開始遊戲", key="start", use_container_width=True):
        st.session_state.game_state['game_running'] = True
        st.session_state.game_state['game_over'] = False
        if len(st.session_state.game_state['foods']) == 0:
            generate_food(st.session_state.game_state)

with col2:
    if st.button("🔄 重新開始", key="reset", use_container_width=True):
        st.session_state.game_state = init_game_state()
        generate_food(st.session_state.game_state)

with col3:
    if st.button("🏁 結束遊戲", key="stop", use_container_width=True):
        st.session_state.game_state['game_running'] = False

# 方向控制
st.markdown("### 🎮 方向控制")

col1, col2, col3 = st.columns([1, 1, 1], gap="small")

with col1:
    if st.button("⬆️ 向上", key="up", use_container_width=True):
        if st.session_state.game_state['direction'][1] == 0:
            st.session_state.game_state['next_direction'] = (0, -1)

with col2:
    if st.button("⬇️ 向下", key="down", use_container_width=True):
        if st.session_state.game_state['direction'][1] == 0:
            st.session_state.game_state['next_direction'] = (0, 1)

st.columns([1])[0].write("")  # 換行

col1, col2, col3 = st.columns([1, 1, 1], gap="small")

with col1:
    if st.button("⬅️ 向左", key="left", use_container_width=True):
        if st.session_state.game_state['direction'][0] == 0:
            st.session_state.game_state['next_direction'] = (-1, 0)

with col3:
    if st.button("➡️ 向右", key="right", use_container_width=True):
        if st.session_state.game_state['direction'][0] == 0:
            st.session_state.game_state['next_direction'] = (1, 0)

# 遊戲顯示
st.markdown("---")

# 初始化食物
if len(st.session_state.game_state['foods']) == 0:
    generate_food(st.session_state.game_state)

# 遊戲迴圈
if st.session_state.game_state['game_running']:
    placeholder = st.empty()

    while st.session_state.game_state['game_running'] and not st.session_state.game_state['game_over']:
        update_game(st.session_state.game_state)

        with placeholder.container():
            draw_game_board(st.session_state.game_state)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("分數", st.session_state.game_state['score'])
            with col2:
                st.metric("最高分", st.session_state.high_score)
            with col3:
                st.metric("難度", st.session_state.game_state['level'])

        time.sleep(0.1)
        st.rerun()

# 非遊戲中的顯示
else:
    draw_game_board(st.session_state.game_state)

# 遊戲結束提示
if st.session_state.game_state['game_over']:
    st.error(f"🎮 遊戲結束！最終分數：{st.session_state.game_state['score']}")
    if st.session_state.game_state['score'] > 0:
        st.info(f"🏆 最高分：{st.session_state.high_score}")

# 遊戲說明
with st.expander("📖 遊戲說明"):
    st.markdown("""
    ### 規則
    - **🟢 綠點**：吃掉後蛇會變長 (+1 節)
    - **🔴 紅點**：吃掉後蛇會變短 (-2 節)
    - **撞牆或撞到自己**：遊戲結束
    
    ### 控制方式
    - 使用按鈕或鍵盤方向鍵控制蛇的方向
    - 點擊「開始遊戲」開始遊戲
    - 點擊「重新開始」重置遊戲
    
    ### 計分
    - 每吃掉一個食物得 10 分
    - 每 100 分升一級，遊戲速度會加快
    """)
