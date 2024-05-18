import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import threading

class YOLOv5GUI:
    def __init__(self, root):
        # 초기화 메서드
        self.root = root
        self.root.title("YOLOv5 GUI")  # 윈도우 제목 설정
        self.training_process = None  # 학습 프로세스 저장 변수 초기화

        # 홈 화면 구성
        self.home_frame = tk.Frame(root)
        self.home_frame.pack(fill="both", expand=True)  # 홈 화면 표시
        tk.Label(self.home_frame, text="YOLOv5 홈 화면", font=("Arial", 16)).pack(pady=20)  # 타이틀 라벨 추가
        tk.Button(self.home_frame, text="1. 학습", command=self.open_train_window, width=20, height=2).pack(pady=10)  # 학습 버튼 추가
        tk.Button(self.home_frame, text="2. 탐지", command=self.open_detect_window, width=20, height=2).pack(pady=10)  # 탐지 버튼 추가

        # 학습 화면 구성
        self.train_frame = tk.Frame(root)
        tk.Button(self.train_frame, text="뒤로가기", command=self.back_to_home).grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.train_frame, text="data.yaml 파일 선택:").grid(row=1, column=0, padx=10, pady=10)
        self.data_yaml_path = tk.Entry(self.train_frame, width=50)
        self.data_yaml_path.grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.train_frame, text="찾아보기", command=self.select_file).grid(row=1, column=2, padx=10, pady=10)
        tk.Label(self.train_frame, text="학습 파일 이름:").grid(row=2, column=0, padx=10, pady=10)
        self.model_name = tk.Entry(self.train_frame, width=50)
        self.model_name.grid(row=2, column=1, padx=10, pady=10)
        tk.Label(self.train_frame, text="저장할 디렉토리 선택:").grid(row=3, column=0, padx=10, pady=10)
        self.save_dir_path = tk.Entry(self.train_frame, width=50)
        self.save_dir_path.grid(row=3, column=1, padx=10, pady=10)
        tk.Button(self.train_frame, text="찾아보기", command=self.select_directory).grid(row=3, column=2, padx=10, pady=10)
        tk.Button(self.train_frame, text="학습 시작", command=self.start_training).grid(row=4, column=1, padx=10, pady=20)
        self.progress_text = tk.Text(self.train_frame, height=10, width=80)
        self.progress_text.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

        # 탐지 화면 구성
        self.detect_frame = tk.Frame(root)
        tk.Button(self.detect_frame, text="뒤로가기", command=self.back_to_home).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(self.detect_frame, text="이미지로 탐지", command=self.open_image_detect_window).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.detect_frame, text="실시간 탐지", command=self.start_realtime_detection).grid(row=1, column=1, padx=10, pady=10)

        # 이미지 탐지 구성
        self.image_detect_frame = tk.Frame(root)
        tk.Button(self.image_detect_frame, text="뒤로가기", command=self.back_to_detect).grid(row=0, column=0, padx=10, pady=10)
        self.image_paths = []
        self.image_list_frame = tk.Frame(self.image_detect_frame)
        self.image_list_frame.grid(row=1, column=0, columnspan=3)
        self.add_image_button = tk.Button(self.image_detect_frame, text="이미지 추가", command=self.add_image).grid(row=2, column=1, padx=10, pady=10)

    def open_train_window(self):
        self.home_frame.pack_forget()
        self.train_frame.pack(fill="both", expand=True)
        self.reset_train_window()

    def open_detect_window(self):
        self.home_frame.pack_forget()
        self.detect_frame.pack(fill="both", expand=True)

    def open_image_detect_window(self):
        self.detect_frame.pack_forget()
        self.image_detect_frame.pack(fill="both", expand=True)
        self.update_image_list()

    def back_to_home(self):
        if self.training_process and self.training_process.poll() is None:
            if messagebox.askyesno("경고", "학습이 진행 중입니다. 취소하시겠습니까?"):
                self.training_process.terminate()
                self.training_process = None
        self.reset_frames()

    def reset_frames(self):
        for frame in [self.train_frame, self.detect_frame, self.image_detect_frame]:
            frame.pack_forget()
        self.home_frame.pack(fill="both", expand=True)

    def add_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")])
        if file_path:
            self.image_paths.append(file_path)
            self.update_image_list()

    def update_image_list(self):
        for widget in self.image_list_frame.winfo_children():
            widget.destroy()
        for idx, path in enumerate(self.image_paths):
            tk.Label(self.image_list_frame, text=path).grid(row=idx, column=0)

    def reset_train_window(self):
        self.data_yaml_path.delete(0, tk.END)
        self.model_name.delete(0, tk.END)
        self.save_dir_path.delete(0, tk.END)
        self.progress_text.delete(1.0, tk.END)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("YAML files", "*.yaml"), ("All files", "*.*")])
        self.data_yaml_path.delete(0, tk.END)
        self.data_yaml_path.insert(0, file_path)

    def select_directory(self):
        dir_path = filedialog.askdirectory()
        self.save_dir_path.delete(0, tk.END)
        self.save_dir_path.insert(0, dir_path)

    def start_training(self):
        data_yaml = self.data_yaml_path.get()
        model_name = self.model_name.get()
        save_dir = self.save_dir_path.get()
        if not data_yaml or not model_name or not save_dir:
            messagebox.showwarning("경고", "모든 필드를 입력해주세요.")
            return
        command = f'python train.py --img 640 --batch 16 --epochs 1 --data {data_yaml} --cfg models/yolov5s.yaml --weights yolov5s.pt --name {model_name} --project {save_dir}'
        self.training_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        threading.Thread(target=self.read_process_output).start()

    def read_process_output(self):
        for line in self.training_process.stdout:
            self.progress_text.insert(tk.END, line)
            self.progress_text.see(tk.END)
        self.training_process.stdout.close()
        self.training_process.wait()
        if self.training_process.returncode == 0:
            messagebox.showinfo("완료", "학습이 완료되었습니다.")
        else:
            messagebox.showerror("오류", "학습 중 오류가 발생했습니다.")
        self.training_process = None

    def back_to_detect(self):
        self.image_detect_frame.pack_forget()
        self.detect_frame.pack(fill="both", expand=True)

    def start_realtime_detection(self):
        # Implement realtime detection functionality here
        pass

if __name__ == "__main__":
    root = tk.Tk()  # Tkinter 루트 윈도우 생성
    app = YOLOv5GUI(root)  # YOLOv5 GUI 앱 생성
    root.mainloop()  # Tkinter 메인 루프 실행
