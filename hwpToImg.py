import os  # 파일과 폴더이름을 다루기 편한 모듈
from tkinter import Tk  # 내장 GUI, 실행이 간편함
from tkinter.filedialog import askopenfilename  # 1개의 파일 선택창
from time import sleep  # 잠시 쉬어주기 위한 함수
import win32com.client as win32  # 한/글을 열기 위한 모듈
import pyperclip as cb


def 제목문자열_추출(hwp):
    hwp.InitScan()  # 문서 탐색 시작
    del_num = 0
    while True:
        result = hwp.GetText()  # 문단별로 텍스트와 상태코드 얻기
        if result[0] == 1:  # 상태코드1 == 문서 끝에 도달하면
            break  # while문 종료
        elif result[0] == 4 and result[1].startswith("증빙자료 번호"):  # 상태코드3:표 내부, 4:표 안으로 진입,
            hwp.MovePos(201)  # 탐색된 위치로 캐럿 이동
            hwp.HAction.Run("TableCellBlock")
            hwp.HAction.Run("TableLowerCell")
            hwp.HAction.Run("Copy")
            number = cb.paste().strip().replace(")", "_")
            hwp.HAction.Run("TableRightCell")
            hwp.HAction.Run("Copy")
            hwp.HAction.Run("Cancel")
            title = cb.paste().strip()
            break
        else:  # 그 외에는
            pass  # 그냥 넘어감
    return (number+title).strip()


if __name__ == '__main__':
    root = Tk()  # GUI 실행하고
    # 소스 한/글파일 선택 -> source_hwp에 전체경로 지정
    source_hwp = askopenfilename(title="아래아한글 파일을 선택해주세요.",
                                 initialdir=os.getcwd(),
                                 filetypes=[("아래아한글파일", "*.hwp *.hwpx")])
    root.destroy()  # GUI 종료

    filename = os.path.basename(source_hwp)  # hwp파일의 전체경로 중 파일이름만 추출
    filepath = os.path.join(os.path.dirname(source_hwp))  # hwp파일의 전체경로 중 경로만 추출
    os.chdir(filepath)  # 해당경로로 이동
    try:
        os.mkdir(filename.rsplit(".", maxsplit=1)[0])  # result 폴더 생성
    except FileExistsError:  # 같은 이름의 폴더가 이미 존재하면
        pass  # 패스
    os.chdir(filename.rsplit(".", maxsplit=1)[0])  # result 폴더로 이동
    filepath = os.getcwd()  # result 폴더의 경로를 filepath 변수로 지정

    hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")  # 한/글 프로그램 실행
    hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModule")  # 보안승인모듈 활성화
    hwp.Open(source_hwp)  # 파일 열기
    hwp.XHwpWindows.Item(0).Visible = False  # 백그라운드작업, True로 바꾸면 숨김해제됨
    hwp.MovePos(2)  # 문서 처음으로 이동
    page_num = hwp.PageCount  # 전체 페이지 수를 page_num에 저장

    for i in range(page_num):  # 페이지 수만큼 반복
        제목 = 제목문자열_추출(hwp)
        hwp.Run("CopyPage")  # 현재쪽 복사
        hwp.Run("DeletePage")  # 현재쪽 삭제
        hwp.XHwpDocuments.Add(isTab=True)  # 새 탭 열기
        hwp.Run("PastePage")  # 붙여넣기
        hwp.Run("MoveTopLevelBegin")  # 문서최상단으로 이동 == hwp.MovePos(2)
        hwp.Run("DeletePage")  # 현재쪽 삭제
        hwp.SaveAs(os.path.join(filepath, 제목 + ".hwp"))  # 기존 파일명+_n.hwp 로 저장
        hwp.XHwpDocuments.Item(0).Close(isDirty=False)  # 탭 닫기
        sleep(0.2)  # 0.1초 쉬어줌(꼭 필요)

    # 완료시 팝업 하나 띄워주기
    msgbox = hwp.XHwpMessageBox
    msgbox.string = f"총 {page_num}개의 파일로 \r\n분할작업이 완료되었습니다."
    msgbox.DoModal()

    # 한/글 닫기
    hwp.XHwpDocuments.Item(0).Close(isDirty=False)  # 원래 문서도 저장하지 않고 닫기
    hwp.Quit()  # 한/글 프로그램 종료