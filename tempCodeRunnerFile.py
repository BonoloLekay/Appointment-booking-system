if __name__ == "__main__":
    app = QApplication(sys.argv)
    window1 = login_tab()
    window1.show()
    sys.exit(app.exec_())