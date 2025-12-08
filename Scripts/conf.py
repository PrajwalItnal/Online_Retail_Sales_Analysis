from Scripts.eda import plt

# 🚀 ENABLE EMOJI SUPPORT IN MATPLOTLIB
def fontConfig():
    plt.rcParams['font.family'] = ['DejaVu Sans', 'Arial Unicode MS', 'Segoe UI Emoji', 'Noto Color Emoji']
    plt.rcParams['axes.unicode_minus'] = False