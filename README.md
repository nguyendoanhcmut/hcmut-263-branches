# HCMUT-263 Interactive Deep Mindmaps (Markmap)

Hệ thống Bản đồ Tư duy Tri thức Chuyên sâu (Subagent Deep Trees) cho các học phần chuyên ngành và kỹ năng tại Trường Đại học Bách khoa – ĐHQG-HCM.

🌐 **Trang tra cứu trực tuyến (GitHub Pages)**: [https://nguyendoanhcmut.github.io/hcmut-263-branches/](https://nguyendoanhcmut.github.io/hcmut-263-branches/)

---

## 📚 Danh mục Học phần

### 1. Kỹ thuật Xử lý Nước thải (Wastewater Treatment Engineering)
- **Truy cập trực tuyến**: [https://nguyendoanhcmut.github.io/hcmut-263-branches/kt-xu-ly-nuoc-thai/](https://nguyendoanhcmut.github.io/hcmut-263-branches/kt-xu-ly-nuoc-thai/)
- **Tệp nguồn Markdown**: [kt-xu-ly-nuoc-thai/wastewater_treatment_deep_branches.md](kt-xu-ly-nuoc-thai/wastewater_treatment_deep_branches.md)
- **Quy mô**: 10 Chương học thuật, 17 phân đoạn chuyên sâu, hơn 14.700 dòng Markdown.
- **Nội dung trọng tâm**:
  - Cơ học: Song chắn rác, lắng cát thổi khí, lắng sơ cấp, DAF, lọc vật liệu hạt.
  - Hóa lý: Keo tụ (Alum, PAC), tạo bông thủy lực/cơ học, khử trùng (Clo, Ozone, UV).
  - Sinh học: Động học vi sinh Monod, bùn hoạt tính hiếu khí (CMAS), nitrat hóa & khử nitrat, phân hủy kỵ khí UASB, khử photpho sinh học nâng cao (EBPR), quản lý và thu hồi tài nguyên bùn cặn theo Metcalf & Eddy.

### 2. Kỹ thuật Xử lý Nước cấp (Water Treatment Engineering)
- **Truy cập trực tuyến**: [https://nguyendoanhcmut.github.io/hcmut-263-branches/kt-xu-ly-nuoc-cap/](https://nguyendoanhcmut.github.io/hcmut-263-branches/kt-xu-ly-nuoc-cap/)
- **Tệp nguồn Markdown**: [kt-xu-ly-nuoc-cap/water_treatment_subagent_deep_branches.md](kt-xu-ly-nuoc-cap/water_treatment_subagent_deep_branches.md)
- **Quy mô**: 8 Chương học thuật, hơn 10.700 dòng Markdown.
- **Nội dung trọng tâm**:
  - Khảo sát chất lượng 4 nguồn nước cấp, kiến trúc mạng lưới 3 phân khu, tiêu chuẩn QCVN 01-1:2018/BYT và TCXDVN 33:2006.
  - Động học keo tụ - tạo bông, bể lắng vách nghiêng lamella, bể lọc nhanh trọng lực hạt xốp, khử trùng Clo tự do / kết hợp, công nghệ khử sắt - mangan và làm mềm nước kết tủa vôi - soda theo giáo trình MWH Crittenden và SAWACO.

### 3. Kỹ năng Lãnh đạo (Leadership Skills - ME4625)
- **Truy cập trực tuyến**: [https://nguyendoanhcmut.github.io/hcmut-263-branches/lanh-dao/](https://nguyendoanhcmut.github.io/hcmut-263-branches/lanh-dao/)
- **Tệp nguồn Markdown**: [lanh-dao/leadership_skills_subagent_deep_branches.md](lanh-dao/leadership_skills_subagent_deep_branches.md)
- **Quy mô**: 10 Chương học thuật, hơn 7.400 dòng Markdown.
- **Nội dung trọng tâm**:
  - Lý thuyết đặc điểm, hành vi, tình huống và chuyển đổi (Transformational Leadership).
  - Kỹ năng giao tiếp và thuyết trình học thuật, tư duy phản biện và mô hình ra quyết định quản trị.
  - Động lực học đội nhóm, quản trị xung đột, lãnh đạo trong môi trường biến động và trách nhiệm đạo đức doanh nghiệp.

---

## 🧭 Cấu trúc Thư mục

```text
hcmut-263-branches/
├── index.html                           # Cổng điều hướng trung tâm (Hub page)
├── README.md                            # Tài liệu hướng dẫn & liên kết trực tuyến
├── kt-xu-ly-nuoc-thai/
│   ├── index.html                       # Bản đồ tư duy xử lý nước thải (Markmap)
│   ├── wastewater_treatment_deep_branches.html
│   ├── wastewater_treatment_deep_branches.md
│   └── fragments/                       # Từng phân đoạn nhỏ theo chương
├── kt-xu-ly-nuoc-cap/
│   ├── index.html                       # Bản đồ tư duy xử lý nước cấp (Markmap)
│   ├── water_treatment_subagent_deep_branches.html
│   ├── water_treatment_subagent_deep_branches.md
│   └── fragments/
└── lanh-dao/
    ├── index.html                       # Bản đồ tư duy kỹ năng lãnh đạo (Markmap)
    ├── leadership_skills_subagent_deep_branches.html
    ├── leadership_skills_subagent_deep_branches.md
    └── fragments/
```

---

## 🛠️ Công nghệ Sử dụng

- **Markmap (D3.js)**: Kết xuất Markdown phân cấp thành cây tư duy đồ họa vector (SVG).
- **KaTeX**: Hiển thị công thức toán học và động học phản ứng mượt mà, chính xác.
- **Responsive Web UI**: Tự động tương thích màn hình điện thoại (iOS, Android), máy tính bảng và máy tính để bàn.
- **Theme Switcher**: Hỗ trợ chế độ Sáng (Light) và Tối (Dark) đồng bộ toàn hệ thống.
