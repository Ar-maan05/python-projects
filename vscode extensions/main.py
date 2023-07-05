import vscode

theme = vscode.ColorTheme(name='my-theme', display_name='My Theme', version='0.0.1')
theme.set_colors(
    background='#12171F',
    foreground='#EFEFEF',
    accent_colors=['#399EF4', '#DA6771', '#4EB071', '#FFF099']
)
vscode.build_theme(theme)