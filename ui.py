import tkinter as tk
from tkinter import filedialog, messagebox, Label
from PIL import Image, ImageTk
import threading
import subprocess
import os

class YOLOv5GUI:
    def __init__(self, root):
        # 초기화 메서드
        self.root = root
        self.root.title("YOLOv5 GUI")  # 윈도우 제목 설정
        self.training_process = None  # 학습 프로세스 저장 변수 초기화
        self.weights_path = None  # 모델 가중치 경로를 저장할 변수
        self.image_paths = []  # 이미지 파일 경로 리스트 초기화

        self.current_image_index = 0  # 현재 보여줄 이미지의 인덱스
        self.photo_images = []  # PhotoImage 객체를 저장할 리스트 추가

        

        # 홈 화면 구성
        self.home_frame = tk.Frame(root)
        self.home_frame.pack(fill="both", expand=True)  # 홈 화면 표시
        tk.Label(self.home_frame, text="체크메이트 홈 화면", font=("Arial", 16)).pack(pady=20)  # 타이틀 라벨 추가
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
        tk.Button(self.detect_frame, text="뒤로가기", command=self.back_to_home_from_detect).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(self.detect_frame, text="이미지로 탐지", command=self.open_image_detect_window).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.detect_frame, text="실시간 탐지", command=self.open_realtime_detect_window).grid(row=1, column=1, padx=10, pady=10)

        # 실시간 탐지 프레임 설정
        self.realtime_detect_frame = tk.Frame(root)
        tk.Button(self.realtime_detect_frame, text="뒤로가기", command=self.back_to_detect).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(self.realtime_detect_frame, text="모델 선택", command=self.select_model).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.realtime_detect_frame, text="실시간 탐지 시작", command=self.start_realtime_detection).grid(row=1, column=1, padx=10, pady=10)
        

        # 이미지 탐지 구성
        self.image_detect_frame = tk.Frame(root)
        tk.Button(self.image_detect_frame, text="뒤로가기", command=self.back_to_detect).grid(row=0, column=0, padx=10, pady=10)
        self.image_list_frame = tk.Frame(self.image_detect_frame)
        self.image_list_frame.grid(row=1, column=0, columnspan=3)
        self.add_image_button = tk.Button(self.image_detect_frame, text="이미지 추가", command=self.add_image).grid(row=2, column=0, padx=10, pady=10)
        self.select_model_button = tk.Button(self.image_detect_frame, text="모델 선택", command=self.select_model).grid(row=2, column=1, padx=10, pady=10)
        self.start_detect_button = tk.Button(self.image_detect_frame, text="탐지 시작", command=self.start_detection).grid(row=2, column=2, padx=10, pady=10)

    def open_realtime_detect_window(self):
        self.detect_frame.pack_forget()
        self.realtime_detect_frame.pack(fill="both", expand=True)
        

    def start_realtime_detection(self):
        if not self.weights_path:
            messagebox.showwarning("경고", "먼저 모델을 선택하세요.")
            return
        command = f'python detect.py --source 0 --weights "{self.weights_path}" --conf 0.5'
        subprocess.Popen(command, shell=True)


    def add_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")])
        if file_path:
            self.image_paths.append(file_path)
            self.update_image_list()


    def select_model(self):
        file_path = filedialog.askopenfilename(title="모델 파일 선택", filetypes=[("Model files", "*.pt"), ("All files", "*.*")])
        if file_path:
            self.weights_path = file_path
            tk.Label(self.image_detect_frame, text=f"선택된 모델: {self.weights_path}").grid(row=3, column=0, columnspan=3)


    def start_detection(self):
        if not self.image_paths or not self.weights_path:
            messagebox.showwarning("경고", "이미지와 모델 파일을 먼저 추가하세요.")
            return
        result_directories = []

        # 각 이미지를 탐지하고 결과 폴더를 수집
        for image_path in self.image_paths:
            command = f'python detect.py --source "{image_path}" --weights "{self.weights_path}" --conf 0.5 --project runs/detect --name exp'
            subprocess.run(command, shell=True)  # Popen에서 run으로 변경하여 동기 실행
            result_directories.append(self.get_latest_results_dir())

        # 모든 결과를 표시
        self.display_results(result_directories)

    def get_latest_results_dir(self):
        base_path = 'runs/detect'
        all_subdirs = [os.path.join(base_path, d) for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
        if not all_subdirs:
            return None
        latest_subdir = max(all_subdirs, key=os.path.getmtime)
        return latest_subdir    
    
    
    def display_results(self, folders):
        if not hasattr(self, 'result_window') or not self.result_window.winfo_exists():
            self.result_window = tk.Toplevel(self.root)
            self.result_window.title("Detection Results")
            self.photo_images = []  # 새 창이 열릴 때마다 이미지 리스트를 초기화
            self.prev_button = tk.Button(self.result_window, text="Previous", command=self.show_prev_image)
            self.prev_button.pack(side=tk.LEFT)
            self.next_button = tk.Button(self.result_window, text="Next", command=self.show_next_image)
            self.next_button.pack(side=tk.RIGHT)

        self.result_images = []
        for folder in folders:
            if folder is None:
                continue
            self.result_images += [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.jpg')]
        
        self.current_image_index = 0
        self.show_image()
    

    def show_image(self):
        if not self.result_images:
            messagebox.showinfo("Info", "No images to display.")
            return
        
        img_path = self.result_images[self.current_image_index]
        img = Image.open(img_path)
        img = img.resize((640, 640), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        self.photo_images.append(photo)  # 레퍼런스 유지를 위해 리스트에 추가

        if hasattr(self, 'image_label'):
            self.image_label.configure(image=photo)
        else:
            self.image_label = tk.Label(self.result_window, image=photo)
            self.image_label.image = photo  # 레이블에 이미지 레퍼런스를 직접 할당
            self.image_label.pack()

    def show_next_image(self):
        if self.current_image_index < len(self.result_images) - 1:
            self.current_image_index += 1
            self.show_image()

    def show_prev_image(self):
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.show_image()


    def update_image_list(self):
        for widget in self.image_list_frame.winfo_children():
            widget.destroy()
        for idx, path in enumerate(self.image_paths):
            tk.Label(self.image_list_frame, text=path).grid(row=idx, column=0)

    def open_train_window(self):
        self.home_frame.pack_forget()
        self.train_frame.pack(fill="both", expand=True)
        self.reset_train_window()

    def open_detect_window(self):
        self.home_frame.pack_forget()
        self.detect_frame.pack(fill="both", expand=True)

    def open_image_detect_window(self):
        self.image_paths.clear()
        self.weights_path = None
        self.detect_frame.pack_forget()
        self.image_detect_frame.pack(fill="both", expand=True)
        self.update_image_list()

    def back_to_home(self):
        if self.training_process and self.training_process.poll() is None:  # 학습이 진행 중인 경우
            if messagebox.askyesno("경고", "학습이 진행 중입니다. 프로그램을 종료하시겠습니까?"):  # 종료 확인 메시지
                self.root.destroy()  # 프로그램 종료
            else:
                return  # 사용자가 '아니오'를 클릭하면 경고창만 닫히고 아무 일도 일어나지 않음
        else:
            self.train_frame.pack_forget()  # 학습 화면 숨기기
            self.home_frame.pack(fill="both", expand=True)  # 홈 화면 표시

    def back_to_home_from_detect(self):
        self.detect_frame.pack_forget()  # 탐지 화면 숨기기
        self.home_frame.pack(fill="both", expand=True)  # 홈 화면 표시

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
        self.realtime_detect_frame.pack_forget()
        self.image_detect_frame.pack_forget()
        self.detect_frame.pack(fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()  # Tkinter 루트 윈도우 생성
    app = YOLOv5GUI(root)  # YOLOv5 GUI 앱 생성
    root.mainloop()  # Tkinter 메인 루프 실행
