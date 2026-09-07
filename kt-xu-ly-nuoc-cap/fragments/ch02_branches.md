## Chương 2: Water Source and Collection System (Công trình thu nước)

### 2.1 Định nghĩa, Chức năng và Phân loại Hệ thống Thu nước (Definition, Role & Classification)
#### 2.1.1 Vai trò Kỹ thuật và Tiêu chí Đánh giá Nguồn nước Thô (Engineering Role & Raw Water Characterization)
##### 2.1.1.1 Định nghĩa Công trình Thu nước Cấp (Engineering Definition of Intake & Collection Systems)
###### Bản chất Thủy lực và Chức năng Giao diện (Hydraulic Interface & Abstraction Reliability)
Công trình thu nước (Raw Water Collection System / Intake Structure) là tổ hợp công trình kỹ thuật đầu mối có nhiệm vụ thu nhận nước an toàn, liên tục và đủ lưu lượng thiết kế ($Q_{\text{design}}$) từ nguồn nước tự nhiên (sông, hồ tự nhiên, hồ chứa nhân tạo, kênh dẫn hoặc các tầng chứa nước ngầm) để chuyển giao vào trạm bơm cấp 1 hoặc tự chảy trực tiếp về trạm xử lý nước cấp (WTP - Water Treatment Plant).

Về mặt thủy lực, công trình thu đóng vai trò là bề mặt ranh giới chuyển tiếp (hydraulic boundary interface) giữa chế độ thủy lực tự nhiên biến động của nguồn nước (thủy triều, dao động mùa lũ/mùa kiệt, xói lở/bồi lắng đáy sông, dòng chảy cuộn sóng) và chế độ dòng chảy nhân tạo có kiểm soát trong hệ thống đường ống công nghệ của nhà máy nước. Yêu cầu tiên quyết là phải đảm bảo khả năng thu nước ổn định ngay cả trong điều kiện bất lợi nhất:
1. Mực nước kiệt thiết kế lịch sử với tần suất bảo đảm $P = 95\% - 97\%$ (theo TCXDVN 33:2006 đối với đô thị loại I và II).
2. Chống chịu được tác động phá hoại của lũ lịch sử với chu kỳ lặp lại 100 năm ($P = 1\%$).
3. Ngăn ngừa triệt để các vật cản nổi, rác kích thước lớn, bùn cát di đáy và sinh vật thủy sinh xâm nhập vào hệ thống bơm.

###### Tiêu chuẩn Chất lượng Nguồn nước Đầu vào (Raw Water Quality Baseline - QCVN 08:2023/BTNMT & QCVN 01-1:2018/BYT)
Chất lượng nguồn nước thô quyết định trực tiếp đến việc lựa chọn công nghệ thu và dây chuyền xử lý tiếp theo:
- **Nguồn nước mặt**: Đánh giá theo **QCVN 08:2023/BTNMT** (Quy chuẩn kỹ thuật quốc gia về chất lượng nước mặt). Nước mặt dùng cho mục đích cấp nước sinh hoạt phải đạt tối thiểu phân hạng A hoặc B1, trong đó các thông số then chốt cần quan trắc nghiêm ngặt bao gồm: Độ đục (Turbidity), Hàm lượng chất lơ lửng (TSS), Nhu cầu oxy sinh hóa ($\text{BOD}_5$), Nhu cầu oxy hóa học ($\text{COD}$), Cacbon hữu cơ tổng số ($\text{TOC}$), Amoni ($\text{NH}_4^+$), Dầu mỡ khoáng, và Coliform tổng số.
- **Nguồn nước ngầm**: Phải kiểm soát chặt chẽ các chỉ tiêu địa hóa học đặc trưng như: Tổng độ cứng ($\text{TH}$ as $\text{CaCO}_3$), Hàm lượng sắt tổng ($\text{Fe}$), Mangan ($\text{Mn}$), Khí hòa tan ($\text{CO}_2$ tự do, $\text{H}_2\text{S}$, $\text{CH}_4$), Amoni, Asen ($\text{As}$), và Clorua ($\text{Cl}^-$) nhằm phòng ngừa hiện tượng xâm nhập mặn.
- **Tiêu chuẩn nước sau xử lý**: Toàn bộ dây chuyền xử lý phải đưa nước đạt quy chuẩn **QCVN 01-1:2018/BYT** (Quy chuẩn kỹ thuật quốc gia về chất lượng nước sạch sử dụng cho mục đích sinh hoạt), cụ thể: Độ đục $\le 2\text{ NTU}$, Màu sắc $\le 15\text{ TCU}$, Sắt tổng $\le 0.3\text{ mg/L}$, Mangan $\le 0.1\text{ mg/L}$, Clorua $\le 250\text{ mg/L}$, và Vi sinh vật ($E. coli$, Coliform) bằng $0\text{ CFU}/100\text{ mL}$.

##### 2.1.1.2 Phân loại Hệ thống Công trình Thu (Intake Classification Taxonomy)
###### Ma trận Đối chiếu Phân loại Công trình Thu (Classification Matrix - Table tbl_ch02_01)
Hệ thống thu nước được phân loại theo hai nhóm nguồn tài nguyên nước chính:

| Phân loại Nhóm Nguồn | Loại Hình Nguồn Nước | Công Nghệ Công Trình Thu | Đặc Điểm Thủy Lực & Địa Chất Cốt Lõi |
| :--- | :--- | :--- | :--- |
| **Surface Water Intake** (Thu nước mặt) | Hồ tự nhiên & Hồ chứa nước (Lakes & Reservoirs) | Tháp thu nước nhiều cửa (Multi-tier Intake Tower), Đầu thu chìm (Submerged Bellmouth) | Tránh phân tầng nhiệt (thermal stratification), tảo nở hoa tầng mặt (algae blooms) và yếm khí tầng đáy (hypolimnetic anoxia). |
| **Surface Water Intake** (Thu nước mặt) | Sông hở & Kênh dẫn (Rivers & Canals) | Trạm thu ven bờ (Shore Intake Station), Công trình thu kết hợp trạm bơm | Đặt tại bờ lõm (bờ xói, luồng sâu), tích hợp song chắn rác thô ($40-50\text{ mm}$) và lưới chắn tinh ($2-10\text{ mm}$). |
| **Surface Water Intake** (Thu nước mặt) | Sông lớn, Giao thông thủy sâu (Navigable Rivers) | Đầu thu đáy sông xa bờ (Offshore Submerged Crib) | Đặt chìm dưới đáy sông ngoài luồng chạy tàu, vận tốc cửa vào thấp ($\le 0.15\text{ m/s}$), dẫn bằng ống tự chảy/si-phông kép. |
| **Surface Water Intake** (Thu nước mặt) | Vùng ven sông bãi bồi (Alluvial Riverbanks) | Hành lang thu nước thấm (Infiltration Gallery), Giếng thu tia Ranney | Khai thác lọc ven bờ (RBF - Riverbank Filtration), giảm độ đục tự nhiên và loại bỏ mầm bệnh bằng tầng alluvium. |
| **Groundwater Collection** (Thu nước ngầm) | Tầng chứa nước không áp tầng nông (Unconfined Aquifer) | Giếng đào đường kính lớn (Dug Wells), Giếng đóng (Driven Well Points) | Chiều sâu $< 15\text{ m}$, ống vách bê tông/thép, lớp lọc sỏi đáy, khai thác quy mô hộ gia đình/cộng đồng nhỏ. |
| **Groundwater Collection** (Thu nước ngầm) | Tầng chứa nước có áp tầng sâu (Confined Aquifer) | Giếng khoan công nghiệp (Deep Drilled Production Wells) | Chiều sâu $30 - 300+\text{ m}$, ống vách thép/PVC, ống lọc khe quấn Johnson, chèn sỏi lọc, trám vữa xi măng cách ly mặt. |
| **Groundwater Pumping** (Cơ điện nâng nước) | Giếng khoan tầng sâu công nghiệp | Bơm chìm đa tầng cánh (Submersible Centrifugal Pump), Bơm tuabin trục đứng | Cụm động cơ-bơm chìm ngập hoàn toàn dưới mực nước động, van một chiều, cột ống đẩy, hiệu suất cao. |
| **Groundwater Pumping** (Cơ điện nâng nước) | Giếng nông phân tán nông thôn | Bơm tay pit-tông tịnh tiến (Reciprocating Hand Pump) | Bơm thể tích hai van một chiều (van chân và van piston), giới hạn hút khí quyển ($6.0 - 7.5\text{ m}$), đòn bẩy cơ học. |

###### Tiêu chí Kinh tế - Kỹ thuật Lựa chọn Phương án Thu (Techno-Economic Selection Criteria)
Việc lựa chọn dạng công trình thu phụ thuộc vào các yếu tố:
1. **Đặc trưng thủy văn nguồn nước mặt**: Biên độ dao động mực nước giữa mùa lũ và mùa cạn ($\Delta H$). Nếu $\Delta H < 3\text{ m}$, có thể dùng công trình thu cố định kiểu ven bờ; nếu $\Delta H > 6\text{ m}$, cần tháp thu nhiều tầng độc lập hoặc trạm bơm nổi (Floating intake/pumping barge).
2. **Địa chất công trình và hình thái bờ**: Độ ổn định chống trượt lở của bờ sông, đặc tính di chuyển bùn cát luồng lạch. Ưu tiên bờ lõm ổn định có nền đá hoặc sét cứng; tránh các doi cát bồi, bãi cạn và vùng lạch quẩn.
3. **Đặc trưng địa chất thủy văn nước ngầm**: Bề dày tầng chứa nước ($B$), hệ số thấm ($K$), hệ số dẫn nước ($T = K \cdot B$), và tính chất áp lực (tầng có áp artesian vs không áp phreatic). Nguồn nước ngầm tầng nông dễ bị tổn thương bởi ô nhiễm bề mặt; nước ngầm tầng sâu đòi hỏi chi phí khoan thăm dò và hoàn thiện giếng lớn.
4. **Quy mô công suất trạm xử lý**: Công suất lớn ($Q > 50,000\text{ m}^3/\text{ngày}$) thường bắt buộc khai thác nước mặt quy mô lớn hoặc bãi giếng khoan cụm liên kết (wellfield) bố trí tối ưu chống tương hỗ hạ thấp mực nước.

---

### 2.2 Công trình Thu Nước Mặt (Surface Water Intake Structures)
#### 2.2.1 Công trình Thu Nước Hồ và Hồ Chứa (Lake & Reservoir Intake Towers)
##### 2.2.1.1 Hiện tượng Phân tầng Nhiệt và Động học Limnology (Thermal Stratification & Limnetic Dynamics)
###### Cấu trúc Phân tầng: Epilimnion, Metalimnion/Thermocline và Hypolimnion
Trong các hồ tự nhiên sâu và hồ chứa thủy điện/thủy lợi nhiệt đới và cận nhiệt đới, bức xạ mặt trời tạo nên sự chênh lệch mật độ nước theo phương đứng, hình thành hiện tượng phân tầng nhiệt mật độ (Thermal Stratification):
1. **Tầng mặt (Epilimnion)**: Tầng nước ấm trên cùng, tiếp xúc trực tiếp với khí quyển và bức xạ mặt trời, nhiệt độ cao ($28 - 32^\circ\text{C}$), nồng độ oxy hòa tan ($\text{DO}$) bão hòa do quang hợp và khuếch tán không khí. Tầng này có mật độ sinh khối tảo, vi khuẩn lam (Cyanobacteria) và chất hữu cơ hòa tan cao nhất.
2. **Tầng chuyển tiếp (Metalimnion / Thermocline)**: Tầng ngăn cách có gradient nhiệt độ giảm đột ngột theo chiều sâu ($> 1^\circ\text{C}$ trên mỗi mét độ sâu). Tầng này đóng vai trò như một màng ngăn thủy lực (density barrier) cản trở sự hòa trộn thẳng đứng giữa tầng mặt và tầng đáy.
3. **Tầng đáy (Hypolimnion)**: Tầng nước sâu, lạnh, thiếu ánh sáng. Do quá trình phân hủy vi sinh vật đối với xác sinh vật chìm xuống từ tầng trên mà không được tái sục khí, nồng độ oxy hòa tan giảm mạnh về $0\text{ mg/L}$ (tình trạng yếm khí - anoxia).

###### Chu kỳ Đảo trộn Nước Hồ (Seasonal Turnover Dynamics)
Vào thời điểm giao mùa (ví dụ cuối thu - đầu đông ở miền Bắc hoặc các đợt bão lớn gió mạnh ở miền Nam), nhiệt độ tầng mặt suy giảm làm mật độ nước tầng trên tăng lên ($\rho_{\text{water}}$ cực đại ở $3.98^\circ\text{C}$). Khi mất gradient mật độ ổn định, năng lượng gió gây ra hiện tượng đảo trộn toàn khối (Seasonal Lake Turnover). Sự đảo trộn đưa toàn bộ bùn đáy giàu sắt, mangan, photpho và khí độc bốc lên toàn bộ cột nước, gây suy giảm đột ngột chất lượng nước cấp vào nhà máy.

###### Động học Hóa - Sinh và Lựa chọn Tầng Khai thác (Limnetic Water Quality Risks)
- **Rủi ro khi lấy nước Tầng mặt (Epilimnion)**:
  - Tảo lam nở hoa tiết ra độc tố vi tảo (Microcystins, Anatoxin-a) gây độc thần kinh và hoại tử gan.
  - Hợp chất hữu cơ gây mùi khó chịu Geosmin và 2-Methylisoborneol (MIB) rất khó xử lý bằng keo tụ thông thường.
  - Hàm lượng tiền chất tạo sản phẩm phụ khử trùng (DBP Precursors: $\text{THMs}$, $\text{HAAs}$) tăng vọt khi khử trùng bằng Clo.
  - Nhiệt độ nước cao làm giảm hiệu quả lắng và tăng nhu cầu clo khử trùng.
- **Rủi ro khi lấy nước Tầng đáy (Hypolimnion)**:
  - Môi trường khử yếm khí thế oxy hóa - khử thấp ($E_h < 0\text{ mV}$) làm hòa tan Sắt ($\text{Fe}^{2+}$) và Mangan ($\text{Mn}^{2+}$) từ khoáng vật trầm tích đáy vào pha lỏng với nồng độ cao ($5 - 20\text{ mg/L}$).
  - Tích tụ khí độc hòa tan có mùi trứng thối và ăn mòn kim loại: $\text{H}_2\text{S}$, Khí Metan ($\text{CH}_4$), Amoni ($\text{NH}_4^+$).
  - Thiếu hụt hoàn toàn oxy hòa tan ($\text{DO} \approx 0$), đòi hỏi chi phí sục khí làm giàu oxy rất tốn kém tại WTP.
- **Vị trí lấy nước tối ưu**: Luôn nằm ở phần dưới của tầng Epilimnion hoặc phần trên của tầng Thermocline, cách xa bề mặt tối thiểu $1.5 - 2.0\text{ m}$ để tránh rác nổi và tảo, đồng thời cách đáy tối thiểu $2.0 - 3.0\text{ m}$ để tránh bùn lắng và nước yếm khí.

##### 2.2.1.2 Kỹ thuật Tháp Thu Nước Nhiều Cửa (Multi-Level Selective Intake Tower Engineering)
###### Cấu tạo Cơ khí Tháp Thu Đa tầng (Tower Mechanical Anatomy)
Tháp thu nước hồ chứa là kết cấu bê tông cốt thép khối lớn hình tròn hoặc đa giác, đặt thẳng đứng trong lòng hồ và nối với bờ bằng cầu công tác (Access bridge - Figure `fig_ch02_001`):
- **Cửa thu đa tầng (Multi-tier intake ports)**: Bố trí ở các cao trình khác nhau dọc theo chiều cao tháp (tối thiểu 3 đến 5 tầng cửa). Mỗi cửa được trang bị lưới chắn rác thô bên ngoài và van đĩa hoặc phai chắn nước (Sluice gates / Stop logs) vận hành bằng tời điện từ sàn công tác trên đỉnh tháp.
- **Khoang thu trung tâm (Wet well chamber)**: Nơi tiếp nhận dòng nước hòa trộn từ cửa thu đang hoạt động, cho phép điều chỉnh lấy nước linh hoạt từ độ sâu có chất lượng nước thô tốt nhất theo mùa.
- **Hệ thống dẫn nước tự chảy (Gravity intake conduits)**: Bố trí ở đáy tháp, dẫn nước bằng trọng lực qua thân đập hoặc xuyên qua lòng hồ về giếng hút trạm bơm cấp 1 đặt trên bờ.

###### Vận tốc Cửa Thu và Thủy lực Chống Xoáy (Intake Port Velocity & Vortex Prevention)
Vận tốc dòng chảy đi qua cửa thu vào tháp phải tuân thủ nghiêm ngặt giới hạn thiết kế:
- Thông số thiết kế: **Lake Intake Tower Selective Port Approach Inflow Velocity** (`dp_ch02_002`):
  $$v_{\text{port}} = 0.15 - 0.30\text{ m/s}$$
- **Mục đích kỹ thuật**:
  1. Giữ chế độ chảy tầng êm dịu, không tạo phễu xoáy bề mặt (air-entraining surface vortices) hút không khí và rác nổi vào tháp gây rung lắc đường ống và giảm lưu lượng bơm.
  2. Tránh cuốn theo sinh vật thủy sinh và cá con di chuyển quanh tháp.
  3. Hạn chế tổn thất cột áp cục bộ qua khe cửa thu ($\Delta h_{\text{port}} < 0.05\text{ m}$).

###### Đường ống Dẫn nước Tự chảy về Trạm Bơm Bờ (Gravity Intake Conduits)
- Thông số thiết kế: **Intake Gravity Conveyance Conduit Flow Velocity** (`dp_ch02_003`):
  $$v_{\text{gravity\_conduit}} = 0.60 - 1.50\text{ m/s}$$
- **Cơ sở xác định**:
  - $v_{\text{min}} \ge 0.60\text{ m/s}$: Vận tốc tự làm sạch (self-cleansing velocity) nhằm ngăn ngừa bùn mịn lắng đọng làm tắc đường ống ngầm dưới đáy hồ.
  - $v_{\text{max}} \le 1.50\text{ m/s}$: Giới hạn tổn thất ma sát đường dài theo phương trình Darcy-Weisbach, hạn chế sụt áp thủy lực và hiện tượng búa nước (water hammer) khi đóng ngắt van khẩn cấp.

###### Công trình Thu Nước Đáy Hồ/Hồ Chứa Submerged Bellmouth (Figure fig_ch02_002)
Đối với các hồ chứa dung tích vừa và nhỏ có chất lượng nước ít biến động theo chiều sâu, có thể sử dụng miệng loa thu nước chìm (Submerged bellmouth intake):
- Miệng loa bằng gang hoặc thép không gỉ đặt ngập sâu dưới mực nước kiệt ít nhất $2.0\text{ m}$ và nâng cao khỏi đáy hồ ít nhất $1.0\text{ m}$.
- Xung quanh miệng loa bọc lồng lưới thép hình nón cụt hoặc quả cầu để ngăn rác và cá.
- Nối trực tiếp với đường ống tự chảy dẫn về trạm bơm bờ.

---

#### 2.2.2 Thủy lực Sông và Nguyên lý Bố trí Công trình Thu (River Intake Hydraulics & Geomorphic Siting)
##### 2.2.2.1 Động lực học Dòng chảy Sông Cong và Vận chuyển Bùn cát (River Fluvial Morphodynamics)
###### Dòng chảy Cuộn Thứ cấp tại Khúc Sông Cong (Secondary Helical Circulation)
Tại các đoạn sông uốn khúc tự nhiên (river meanders), sự kết hợp giữa lực quán tính ly tâm của dòng chảy chính và gradient áp lực hướng tâm do chênh lệch mực nước bề mặt tạo nên chuyển động xoắn cuộn thứ cấp 3 chiều (Helical secondary circulation):
- Ở tầng mặt: Nước có vận tốc cao dạt mạnh về phía bờ ngoài (bờ lõm - Outer concave bank).
- Ở tầng đáy: Nước có vận tốc nhỏ bị lực áp suất hướng tâm đẩy ngược từ bờ lõm sang bờ trong (bờ lồi - Inner convex bank).
- Chuyển động xoắn ốc này liên tục bóc tách và vận chuyển các hạt phù sa, bùn cát từ đáy bờ lõm sang bồi tụ tại bờ lồi.

###### Tuyến Động lực Xói - Bồi: Bờ Lõm (Concave Cut Bank) vs Bờ Lồi (Convex Point Bar)
1. **Bờ lõm (Concave bank / Cut bank)**:
   - Dòng chảy áp sát bờ với vận tốc lớn nhất ($v_{\text{surface}} = v_{\text{max}}$).
   - Đáy sông bị xói sâu tự nhiên hình thành lạch sâu chính (thalweg) ổn định quanh năm.
   - Bùn cát đáy không thể lắng đọng; nước có độ sâu lớn ngay cả trong mùa kiệt khô hạn.
   - **Đây là vị trí lý tưởng nhất để bố trí công trình thu nước mặt ven bờ** (Figure `fig_ch02_003`).
2. **Bờ lồi (Convex bank / Point bar)**:
   - Vận tốc dòng chảy giảm đột ngột, dòng thứ cấp tầng đáy đẩy bùn cát sang tích tụ thành bãi bồi ven bờ.
   - Độ sâu nước rất nông, thường xuyên bồi lấp cửa thu trong mùa lũ và cạn kiệt đáy trong mùa khô.
   - Tuyệt đối không đặt công trình thu cố định tại bờ lồi do nguy cơ tê liệt vì bồi tích phù sa.

###### Đường Luồng Sâu (Thalweg) và Độ sâu Thủy văn Mùa cạn (Dry-Weather Navigational Clearance)
- **Vết luồng sâu (Thalweg)**: Tuyến nối liền các điểm sâu nhất của lòng dẫn sông. Công trình thu phải tiếp cận càng gần thalweg càng tốt để bảo đảm cột nước thu.
- **Tĩnh không an toàn**: Cao trình ngưỡng cửa thu phải thấp hơn mực nước kiệt thiết kế lịch sử ($H_{\text{min, 95\%}}$) tối thiểu $0.5 - 1.0\text{ m}$ để tránh tạo phễu hút khí bề mặt, đồng thời cao hơn đáy sông ổn định tối thiểu $0.5 - 1.0\text{ m}$ để ngăn ngừa bùn cát di đáy (bedload sediment transport) xâm nhập.

##### 2.2.2.2 Vị trí Sắp đặt và Vành đai Bảo vệ Vệ sinh Công trình Thu (Intake Siting & Sanitary Zones)
###### Tiêu chí Định vị Thượng lưu Nguồn Thải
1. Công trình thu nước phải luôn đặt ở **phía thượng lưu** khu dân cư đô thị, khu công nghiệp tập trung, cửa xả nhà máy xử lý nước thải và âu tàu/bến cảng giao thông thủy.
2. Tránh các khu vực nước quẩn, khúc sông phân nhánh có bãi bồi di động, hoặc hạ lưu các cửa sông đổ phù sa lớn.

###### Vùng Bảo hộ Vệ sinh Nguồn nước Mặt theo TCXDVN 33:2006
Để bảo đảm an toàn sinh học và ngăn ngừa ô nhiễm độc chất, tiêu chuẩn **TCXDVN 33:2006** quy định nghiêm ngặt 2 cấp vùng bảo hộ vệ sinh:
- **Vùng bảo hộ cấp I (Vùng bảo vệ nghiêm ngặt)**:
  - Phạm vi: Bán kính $100 - 200\text{ m}$ về phía thượng lưu và $50 - 100\text{ m}$ về phía hạ lưu cửa thu; từ mép bờ ra lòng sông tối thiểu $50\text{ m}$ hoặc đến tim luồng chạy tàu.
  - Quy định: Cắm biển báo phao tiêu bảo vệ, rào chắn; nghiêm cấm tuyệt đối mọi hoạt động tắm giặt, xả nước thải, xây dựng công trình, chăn nuôi thủy sản, neo đậu tàu thuyền và thả lưới đánh bắt cá.
- **Vùng bảo hộ cấp II (Vùng hạn chế ô nhiễm)**:
  - Phạm vi: Tối thiểu $1,000 - 2,000\text{ m}$ về phía thượng lưu và $200 - 500\text{ m}$ về phía hạ lưu công trình thu.
  - Quy định: Cấm xả nước thải chưa qua xử lý đạt chuẩn loại A; cấm kho bãi chứa hóa chất độc hại, phân bón vô cơ, thuốc bảo vệ thực vật, nghĩa trang và bãi chôn lấp chất thải rắn.

---

#### 2.2.3 Trạm Thu Nước Ven Bờ và Hệ thống Lưới Chắn Rác (Shore Intake Stations & Screening Facilities)
##### 2.2.3.1 Cấu tạo Tổng thể Trạm Thu Ven Bờ (Shore Intake Station Architecture)
Trạm thu nước ven bờ kết hợp trạm bơm cấp 1 là công trình bê tông cốt thép khối lớn kiên cố xây dựng trực tiếp tại mép bờ dốc ổn định (Figure `fig_ch02_004`). Công trình được phân chia thành các ngăn độc lập vận hành song song:
1. **Buồng thu thô (Coarse screen chamber)**: Đặt song chắn rác thô (trash racks) bảo vệ mặt trước chống củi gỗ, rác nổi lớn.
2. **Buồng lưới chắn tinh (Fine traveling water screen chamber)**: Đặt lưới chắn rác cơ động tinh dạng băng chuyền để loại bỏ rác nhỏ, rong rêu, bèo tấm.
3. **Ngăn hút trạm bơm (Suction wet well / Pump sump)**: Không gian thủy lực êm dịu chứa nước sạch sau lưới lọc, là nơi đặt ống hút của máy bơm ly tâm trục đứng hoặc trục ngang.
4. **Nhà trạm trên mặt đất**: Chứa động cơ điện, cầu trục nâng hạ, tủ biến tần điều khiển và hệ thống máy ép rác, vòi rửa phản lực.

##### 2.2.3.2 Song Chắn Rác Thô và Tổn Thất Thủy Lực Kirschmer (Coarse Trash Bar Racks & Kirschmer Head Loss)
###### Cấu tạo Cơ khí Song Chắn Rác
- Thông số: **Coarse Trash Bar Rack Clear Spacing** (`dp_ch02_004`):
  $$b_{\text{coarse}} = 40 - 50\text{ mm} \quad (\text{hoặc } 25 - 50\text{ mm tùy nguồn rác})$$
- Vật liệu chế tạo: Thép không gỉ (SUS 304/316) hoặc thép carbon mạ kẽm nhúng nóng, tiết diện thanh hình chữ nhật dày $s = 8 - 12\text{ mm}$ (tiêu chuẩn $s = 10\text{ mm}$).
- Góc nghiêng lắp đặt: $\alpha = 60^\circ - 75^\circ$ so với phương ngang để tạo thuận lợi cho cào rác thủ công hoặc lưỡi cào cơ giới (mechanical rakes) trục kéo gầu.

###### Phương trình Thủy lực Kirschmer Tính Tổn Thất Cột Nước qua Song Chắn (Kirschmer Equation)
Tổn thất cột nước qua song chắn rác sạch được xác định chính xác theo phương trình bán thực nghiệm Kirschmer:

$$\text{Phương trình Kirschmer: } h_L = \beta \cdot \left(\frac{s}{b}\right)^{4/3} \cdot \frac{v_0^2}{2g} \cdot \sin(\alpha)$$

- **Mã phương trình**: `eq_ch02_008`
- **Ý nghĩa các biến số**:
  - $h_L$: Tổn thất cột nước qua song chắn rác ($\text{m}$).
  - $\beta$: Hệ số hình dạng thanh chắn (Kirschmer bar shape factor, không thứ nguyên):
    - Thanh chữ nhật cạnh sắc (Sharp-edged rectangular): $\beta = 2.42$.
    - Thanh chữ nhật bo tròn đầu (Semi-circular ends / Rounded rectangular): $\beta = 1.79$.
    - Thanh hình tròn hoàn toàn (Circular cylindrical bar): $\beta = 1.67$ (hoặc $0.76 - 1.07$ tùy tỷ lệ bố trí).
    - Thanh hình giọt nước khí động học (Teardrop shape): $\beta = 0.76$.
  - $s$: Bề dày của thanh chắn đón hướng dòng chảy ($\text{m}$ hoặc $\text{mm}$).
  - $b$: Khoảng cách lọt lòng giữa hai thanh liền kề ($\text{m}$ hoặc $\text{mm}$).
  - $v_0$: Vận tốc dòng chảy trong kênh tiếp cận ngay trước song chắn ($\text{m/s}$). Tiêu chuẩn vận tốc tiếp cận: $v_0 = 0.60 - 1.00\text{ m/s}$.
  - $g$: Gia tốc trọng trường ($9.81\text{ m/s}^2$).
  - $\alpha$: Góc nghiêng của thanh chắn so với mặt phẳng nằm ngang ($^\circ$).

###### Hiện tượng Nghẹt Rác và Hệ số An Toàn
Trong quá trình vận hành mùa mưa lũ, rác bám tích tụ làm giảm diện tích thông nước hữu hiệu. Khi tính toán thủy lực thiết kế ngăn trạm thu, bắt buộc phải kiểm tra điều kiện song chắn bị nghẹt $50\%$ diện tích ($b_{\text{eff}} = 0.5 \cdot b$). Lúc này tổn thất cột áp $h_{L,\text{clogged}}$ tăng vọt khoảng $2.5 - 3.0$ lần so với trạng thái sạch, đòi hỏi cao trình tường ngăn và rãnh tràn phải có độ cao dự phòng an toàn (freeboard) tối thiểu $0.3 - 0.5\text{ m}$.

##### 2.2.3.3 Lưới Chắn Rác Tinh Cơ Động và Tiêu Chuẩn Bảo Vệ Thủy Sinh (Fine Traveling Screens & Fish Protection)
###### Cơ cấu Hoạt động của Lưới Chắn Rác Tinh Cơ Động (Traveling Water Screen Mechanism)
Nước sau khi qua song chắn thô được dẫn qua lưới chắn rác cơ động tinh (Traveling Water Screen):
- Cấu tạo: Chuỗi các tấm lưới đan mắt vuông bằng thép không gỉ (kích thước mắt lưới $b_{\text{fine}} = 2 - 10\text{ mm}$, tiêu chuẩn $5 - 6\text{ mm}$ - `dp_ch02_005`) gắn trên hai dải xích truyền động thẳng đứng vô tận.
- Nguyên lý: Lưới chuyển động tịnh tiến liên tục từ dưới đáy lên sàn trạm thu với vận tốc chậm ($1.5 - 3.0\text{ m/phút}$). Khi các tấm lưới dính rác lên đến đỉnh tháp, dàn vòi phun tia nước áp lực cao ($p = 3 - 5\text{ bar}$) từ phía sau sẽ thổi bay toàn bộ rác vào máng thu gom để đưa về máy ép bùn rác.

###### Phương trình Vận tốc Tiếp cận qua Lưới Chắn Rác (Through-Slot Velocity Equation)
Vận tốc dòng chảy thực tế đi qua diện tích mở của lưới chắn rác được khống chế theo công thức:

$$\text{Vận tốc qua lưới: } v_{\text{screen}} = \frac{Q}{A_{\text{net}}} = \frac{Q}{A_{\text{gross}} \cdot (1 - \text{fraction}_{\text{solid}})} \le 0.15\text{ m/s}$$

- **Mã phương trình**: `eq_ch02_007`
- **Ý nghĩa các biến số**:
  - $v_{\text{screen}}$: Vận tốc tiếp cận xuyên qua mắt lưới hữu hiệu ($\text{m/s}$).
  - $Q$: Lưu lượng nước thô khai thác của trạm thu ($\text{m}^3/\text{s}$).
  - $A_{\text{net}}$: Diện tích thông thủy thực tế của các lỗ lưới nằm dưới mực nước kiệt ($\text{m}^2$).
  - $A_{\text{gross}}$: Diện tích hình học tổng thể phần ngập nước của khung lưới ($\text{m}^2$).
  - $\text{fraction}_{\text{solid}}$: Tỷ lệ diện tích bị cản trở bởi sợi kim loại đan và khung đỡ (thường chiếm $40\% - 55\%$, tương ứng diện tích mở tự do $C_{\text{open}} = 45\% - 60\%$).

###### Tiêu chuẩn Bảo vệ Cá US EPA 316(b) & TCXDVN 33:2006
- Thông số: **Surface Water Intake Screen Through-Slot Approach Velocity** (`dp_ch02_001`):
  $$v_{\text{intake\_screen}} \le 0.15\text{ m/s} \quad (\approx 0.5\text{ ft/s})$$
- **Cơ sở sinh thái học**: Tiêu chuẩn môi trường quốc tế **US EPA 316(b)** (Clean Water Act) và **TCXDVN 33:2006** quy định nghiêm ngặt vận tốc tiếp cận bề mặt lưới không được vượt quá $0.15\text{ m/s}$. Ở vận tốc cực nhỏ này, các loài cá con, tôm và sinh vật thủy sinh có đủ sức bơi ngược dòng (burst swimming speed) để thoát khỏi lực hút của miệng thu, ngăn ngừa triệt để hiện tượng cá bị ép chết dính vào mặt lưới (fish impingement) hoặc bị hút chui qua mắt lưới vào guồng bơm (fish entrainment).

##### 2.2.3.4 Quy trình Thiết Kế Thủy Lực Trạm Thu Ven Bờ (Procedure proc_ch02_01)
Trình tự tính toán định cỡ trạm thu nước ven bờ gồm 4 bước kỹ thuật:
1. **Bước 1: Khảo sát thủy văn và định vị công trình (Site Siting)**:
   Xác định vị trí bờ lõm ổn định của sông, cách xa nguồn thải thượng lưu. Thu thập số liệu mực nước lũ cao nhất ($H_{\text{max}, 1\%}$), mực nước kiệt thấp nhất ($H_{\text{min}, 95\%}$) và đường đo sâu lòng sông (bathymetry).
2. **Bước 2: Định cỡ buồng và song chắn rác thô (Coarse Bar Rack Sizing)**:
   Chọn bề dày thanh $s = 10\text{ mm}$, khoảng cách lọt lòng $b = 40\text{ mm}$, góc nghiêng $\alpha = 75^\circ$. Chọn vận tốc tới gần $v_0 = 0.60 - 0.80\text{ m/s}$. Tính diện tích thông thủy cần thiết và bề rộng khoang dẫn. Áp dụng phương trình Kirschmer kiểm tra tổn thất áp lực ở trạng thái sạch và trạng thái nghẹt $50\%$.
3. **Bước 3: Định cỡ lưới chắn rác cơ động tinh (Fine Traveling Screen Sizing)**:
   Chọn kích thước mắt lưới $b_{\text{fine}} = 2 - 6\text{ mm}$. Áp dụng tiêu chuẩn vận tốc tiếp cận $v_{\text{screen}} \le 0.15\text{ m/s}$. Tính toán diện tích hình học ngập nước tổng thể $A_{\text{gross}} = Q / [v_{\text{screen}} \cdot (1 - \text{fraction}_{\text{solid}})]$. Lựa chọn số lượng mô-đun lưới vận hành song song kèm $1$ mô-đun dự phòng ($N + 1$).
4. **Bước 4: Định cỡ ngăn hút và ống hút trạm bơm (Pump Wet Well Sizing)**:
   Thiết kế ngăn hút trạm bơm theo tiêu chuẩn Thủy lực Viện Thủy lực Hoa Kỳ (Hydraulic Institute Standards - HIS). Đảm bảo thời gian lưu nước tối thiểu $t = 2 - 3\text{ phút}$ để khử bọt khí; khoảng cách từ đáy ống hút đến đáy giếng $C = (0.3 - 0.5) \cdot D_{\text{bell}}$, độ sâu ngập nước tối thiểu của miệng loe $S > D_{\text{bell}} + 1.5 \cdot (v^2/2g)$ để chống xoáy khí.

##### 2.2.3.5 Bài Tập Tính Toán Điển Hình Trạm Thu Ven Bờ (Worked Example EX-CH02-05)
###### Đề bài (Problem Statement)
Một trạm xử lý nước cấp đô thị cần lấy nước từ sông qua một trạm thu ven bờ với lưu lượng thiết kế $Q = 54,000\text{ m}^3/\text{ngày}$ ($0.625\text{ m}^3/\text{s}$). 
Song chắn rác thô được chế tạo bằng các thanh thép hình chữ nhật cạnh sắc dày $s = 10\text{ mm}$, khoảng cách lọt lòng giữa các thanh $b = 40\text{ mm}$ (hệ số hình dạng Kirschmer $\beta = 2.42$). Song chắn được đặt nghiêng một góc $\alpha = 75^\circ$ so với mặt phẳng nằm ngang. Vận tốc tiếp cận của dòng nước trong kênh dẫn phía trước song chắn là $v_0 = 0.60\text{ m/s}$ và chiều sâu lớp nước trong kênh ứng với mực nước kiệt là $H = 2.50\text{ m}$.
Phía sau song chắn rác thô là hệ thống lưới chắn rác cơ động tinh dạng băng chuyền với tỷ lệ diện tích mở thông thủy là $45\%$ ($C_{\text{fine, open}} = 0.45$). Lưới phải tuân thủ tiêu chuẩn bảo vệ cá US EPA 316(b) với vận tốc tiếp cận tối đa cho phép $v_{\text{fine, max}} \le 0.15\text{ m/s}$.
Hãy tính toán:
1. Bề rộng thông thủy ròng và bề rộng tổng thể thiết kế của kênh dẫn song chắn rác thô.
2. Tổn thất cột nước thủy lực qua song chắn rác thô ở trạng thái hoàn toàn sạch ($h_{L,\text{clean}}$).
3. Tổn thất cột nước qua song chắn rác thô giả định khi bị rác bám nghẹt $50\%$ khoảng cách khe ($h_{L,\text{clogged}}$).
4. Diện tích ngập nước tổng thể tối thiểu ($A_{\text{gross}}$) của bề mặt lưới chắn rác tinh.

###### Thông số cho trước (Given Data)
- Lưu lượng nước khai thác $Q = 0.625\text{ m}^3/\text{s}$.
- Chiều dày thanh chắn $s = 0.010\text{ m}$ ($10\text{ mm}$).
- Khoảng cách khe hở $b = 0.040\text{ m}$ ($40\text{ mm}$).
- Hệ số Kirschmer thanh chữ nhật $\beta = 2.42$.
- Góc nghiêng $\alpha = 75.0^\circ$.
- Vận tốc tới gần $v_0 = 0.60\text{ m/s}$.
- Chiều sâu cột nước mùa kiệt $H = 2.50\text{ m}$.
- Tỷ lệ diện tích mở lưới tinh $C_{\text{fine, open}} = 0.45$.
- Vận tốc tối đa qua lưới tinh $v_{\text{fine, max}} = 0.15\text{ m/s}$.

###### Lời giải Chi tiết Từng bước (Step-by-Step Solution)
- **Bước 1: Tính bề rộng kênh dẫn qua song chắn rác thô**:
  - Diện tích mặt cắt ướt của dòng nước trong kênh tiếp cận:
    $$A_{\text{net}} = \frac{Q}{v_0} = \frac{0.625}{0.60} = 1.0417\text{ m}^2$$
  - Bề rộng thông thủy hữu hiệu của dòng nước:
    $$W_{\text{net}} = \frac{A_{\text{net}}}{H} = \frac{1.0417}{2.50} = 0.4167\text{ m}$$
  - Hệ số co hẹp dòng do các thanh chắn chiếm chỗ:
    $$\phi = \frac{b}{s + b} = \frac{40}{10 + 40} = \frac{40}{50} = 0.80$$
  - Bề rộng tổng thể hình học của kênh dẫn song chắn rác:
    $$W_{\text{gross}} = \frac{W_{\text{net}}}{\phi} = \frac{0.4167}{0.80} = 0.5208\text{ m}$$
  - Trong thực tế thiết kế, quy chuẩn chọn bề rộng xây dựng bo tròn: $W_{\text{design}} = 0.60\text{ m}$.

- **Bước 2: Tính tổn thất cột nước qua song chắn rác sạch ($h_{L,\text{clean}}$)**:
  - Áp dụng công thức Kirschmer (`eq_ch02_008`):
    $$h_L = \beta \cdot \left(\frac{s}{b}\right)^{4/3} \cdot \frac{v_0^2}{2g} \cdot \sin(\alpha)$$
  - Tỷ số hình học:
    $$\frac{s}{b} = \frac{10}{40} = 0.25 \implies (0.25)^{4/3} = 0.15749$$
  - Cột áp lưu tốc tới gần:
    $$\frac{v_0^2}{2g} = \frac{(0.60)^2}{2 \times 9.81} = \frac{0.36}{19.62} = 0.018349\text{ m}$$
  - Thành phần góc nghiêng:
    $$\sin(75^\circ) = 0.965926$$
  - Thay số:
    $$h_{L,\text{clean}} = 2.42 \times 0.15749 \times 0.018349 \times 0.965926 = 0.006756\text{ m} \approx 6.76\text{ mm}$$

- **Bước 3: Tính tổn thất cột nước khi song chắn bị nghẹt 50% ($h_{L,\text{clogged}}$)**:
  - Khi rác bám nghẹt $50\%$ khe hở, khoảng cách khe lọt lòng hiệu dụng giảm còn:
    $$b_{\text{clogged}} = 0.50 \times 40\text{ mm} = 20\text{ mm} = 0.020\text{ m}$$
  - Tỷ số hình học mới:
    $$\frac{s}{b_{\text{clogged}}} = \frac{10}{20} = 0.50 \implies (0.50)^{4/3} = 0.39685$$
  - Thay số tính tổn thất cột nước:
    $$h_{L,\text{clogged}} = 2.42 \times 0.39685 \times 0.018349 \times 0.965926 = 0.017024\text{ m} \approx 17.04\text{ mm}$$
  - *Nhận xét*: Tổn thất cột áp tăng gấp $17.04 / 6.76 = 2.52$ lần. Khi nghẹt nặng hơn ($70-80\%$), tổn thất sẽ vượt quá $100\text{ mm}$, kích hoạt tín hiệu cảm biến chênh áp để tự động khởi động máy cào rác.

- **Bước 4: Định cỡ bề mặt ngập nước của lưới chắn rác tinh**:
  - Diện tích thông thủy ròng yêu cầu qua các mắt lưới:
    $$A_{\text{fine, net}} = \frac{Q}{v_{\text{fine, max}}} = \frac{0.625}{0.15} = 4.1667\text{ m}^2$$
  - Diện tích ngập nước tổng thể của khung lưới chắn tinh:
    $$A_{\text{gross}} = \frac{A_{\text{fine, net}}}{C_{\text{fine, open}}} = \frac{4.1667}{0.45} = 9.259\text{ m}^2$$
  - Với chiều sâu ngập nước mùa kiệt $H = 2.50\text{ m}$, bề rộng tối thiểu của băng tải lưới tinh:
    $$B_{\text{screen}} = \frac{9.259}{2.50} = 3.70\text{ m}$$
  - Phương án bố trí: Lựa chọn $2$ giàn lưới chắn rác cơ động tinh vận hành song song, mỗi giàn có bề rộng tiêu chuẩn $2.0\text{ m}$ (tổng bề rộng $4.0\text{ m} > 3.70\text{ m}$, đạt chuẩn an toàn).

###### Đáp số (Final Answer)
- Bề rộng thông thủy tính toán $W = 0.52\text{ m}$ (chọn bề rộng thiết kế $W_{\text{design}} = 0.60\text{ m}$).
- Tổn thất cột áp qua song chắn sạch: $h_{L,\text{clean}} = 6.76\text{ mm}$ ($0.00676\text{ m}$).
- Tổn thất cột áp khi nghẹt $50\%$: $h_{L,\text{clogged}} = 17.04\text{ mm}$ ($0.01704\text{ m}$).
- Diện tích ngập nước tổng thể tối thiểu của lưới tinh: $A_{\text{gross}} = 9.26\text{ m}^2$ (bố trí 2 mô-đun $B = 2.0\text{ m}$).

---

#### 2.2.4 Công Trình Thu Nước Xa Bờ và Đầu Thu Đáy Sông (Offshore Riverbed Intakes & Submerged Cribs)
##### 2.2.4.1 Kỹ thuật Đầu Thu Đáy Sông Submerged Crib (Offshore Submerged Crib Engineering)
###### Cấu tạo Khung Đầu Thu (Intake Crib Structure)
Đối với các dòng sông lớn có biên độ mực nước không quá lớn nhưng luồng chạy tàu nằm cách xa bờ hoặc vùng ven bờ bị bồi lắng cạn kiệt, giải pháp tối ưu là xây dựng đầu thu chìm xa bờ (Submerged Crib Intake):
- Kết cấu: Khối lồng bê tông cốt thép đúc sẵn hình lăng trụ lục giác hoặc bát giác, bên trong chứa đá hộc gia tải để chống lật do dòng lũ. Phía trên đỉnh và xung quanh miệng thu bọc các nan thép chấn song chắn rác thô hoặc nắp nón chống dòng xoáy (vortex suppressor plate).
- Chiều cao đặt: Ngưỡng thu nước phải cao hơn đáy sông tự nhiên ít nhất $0.5 - 1.0\text{ m}$ để ngăn phù sa di đáy chui vào ống, đồng thời đỉnh công trình phải nằm sâu dưới mực nước thông thuyền thấp nhất ít nhất $2.0 - 3.0\text{ m}$ để bảo đảm an toàn giao thông thủy.

###### Khống chế Vận tốc Dòng Vào Cực thấp ($\le 0.15\text{ m/s}$)
Để tránh biến đầu thu thành một "máy hút bụi" hút toàn bộ cá con, rác chìm và bùn cát lơ lửng vào đường ống, vận tốc dòng chảy qua các khe nan của đầu thu xa bờ được khống chế ở mức cực thấp: $v_{\text{crib}} \le 0.10 - 0.15\text{ m/s}$.

##### 2.2.4.2 Tuyến Đường Ống Dẫn Nước Thô Đáy Sông (Raw Water Intake Conduits: Gravity vs Siphon)
Nước từ đầu thu xa bờ được dẫn vào giếng thu ven bờ bằng hai phương án thủy lực:
1. **Tuyến ống tự chảy trọng lực kép (Dual Gravity Pipelines)**:
   - Đặt ngập sâu dưới đáy sông trong rãnh đào được bọc đá hộc bảo vệ chống xói lở và neo tàu móc neo.
   - Bắt buộc phải đặt tối thiểu $2$ đường ống chạy song song độc lập (tiêu chuẩn dự phòng $N-1$). Khi một đường ống bị sự cố vỡ hoặc súc rửa cát bùn, đường ống còn lại vẫn phải đảm bảo cung cấp tối thiểu $70\% - 75\%$ công suất thiết kế của trạm xử lý.
   - Vận tốc dòng chảy trong ống: $v = 0.60 - 1.50\text{ m/s}$ (`dp_ch02_003`) để chống lắng cặn.
2. **Tuyến ống xi-phông (Siphon Pipelines)**:
   - Áp dụng khi bờ sông có địa hình cao hoặc đê bao kiên cố không thể đào xuyên qua để đặt ống tự chảy.
   - Điểm cao nhất của ống xi-phông nằm trên đỉnh đê, cao hơn mực nước kiệt của sông.
   - Đòi hỏi phải có hệ thống bơm hút chân không (Vacuum priming system) tự động để duy trì độ chân không liên tục, trục xuất túi khí tích tụ ở đỉnh ống và mồi nước khi khởi động hệ thống. Độ cao xi-phông chân không tuyệt đối không được vượt quá $5.0 - 6.0\text{ m}$ để tránh đứt đoạn dòng thủy lực do nước sôi tạo bọt khí ở áp suất chân không.

---

### 2.3 Công Trình Thu Nước Ngầm Tầng Nông và Hành Lang Lọc Ven Bờ (Shallow Groundwater Systems & Infiltration Galleries)
#### 2.3.1 Giếng Đào Đường Kính Lớn (Large-Diameter Dug Wells)
##### 2.3.1.1 Cấu tạo và Cơ Chế Tích Trữ Thủy Lực (Dug Well Structural Anatomy & Well Storage)
Giếng đào là công trình thu nước ngầm cổ truyền nhưng vẫn giữ vai trò chiến lược ở vùng nông thôn và bán sơn địa:
- Thông số: **Shallow Dug Well Internal Diameter** (`dp_ch02_011`):
  $$D_{\text{dug\_well}} = 1.0 - 3.0\text{ m}$$
- Thông số: **Shallow Dug Well Typical Excavation Depth** (`dp_ch02_012`):
  $$H_{\text{dug\_well}} = 5 - 15\text{ m}$$
- **Ống vách và Thành giếng**: Xây bằng gạch thẻ liên kết vữa xi măng mác cao hoặc xếp các ống tròn bê tông cốt thép đúc sẵn (precast concrete rings) có gờ âm dương chèn gioăng kín nước (Figure `fig_ch02_005`).
- **Lớp lọc ngược đáy giếng (Inverted gravel filter bed)**: Đáy giếng đào sâu vào tầng cát chứa nước phải được trải lớp lọc ngược 3 tầng: tầng cát thô ($d = 1 - 2\text{ mm}$ dày $10\text{ cm}$), tầng sỏi nhỏ ($d = 5 - 10\text{ mm}$ dày $10\text{ cm}$), và tầng cuội sỏi ($d = 20 - 40\text{ mm}$ dày $15\text{ cm}$). Lớp lọc này có vai trò sống còn triệt tiêu lực thấm hướng lên, ngăn chặn hoàn toàn hiện tượng cát đùn, cát chảy (quicksand / boiling condition) làm sụp lún thành giếng.
- **Dung tích trữ trong giếng (Well In-situ Storage)**: Ưu điểm nổi bật của giếng đào đường kính lớn là cung cấp thể tích đệm trữ nước rất lớn bên trong giếng ($V = \pi D^2 H_w / 4 \approx 5 - 20\text{ m}^3$). Điều này cho phép khai thác nước ngầm từ các tầng chứa nước có hệ số thấm rất bé ($K < 1\text{ m/ngày}$) bằng cách tích trữ nước thấm chậm vào ban đêm và bơm hút với công suất lớn vào ban ngày.

##### 2.3.1.2 Kỹ thuật Thi công Giếng Chìm và Bảo Vệ Vệ Sinh Đầu Giếng (Caisson Sinking & Sanitary Protection)
###### Phương pháp Thi công Hạ Giếng Chìm (Caisson Sinking Method - Figure fig_ch02_008)
Để đào giếng trong tầng cát pha ngậm nước mà vách đất không bị sạt lở:
1. Đặt vành dao thép chịu lực (cutting shoe) dưới đáy đốt ống bê tông đầu tiên.
2. Công nhân đào bới đất thủ công hoặc máy đào gầu ngoạm vét đất từ tâm lòng giếng lên.
3. Trọng lượng bản thân của các đốt ống bê tông kết hợp tải trọng chất thêm làm đốt ống tự tụt chìm dần xuống đất. Khi ống chìm ngang mặt đất, lắp ráp tiếp đốt ống thứ hai lên trên và lặp lại quá trình cho đến khi đạt độ sâu tầng chứa nước thiết kế.

###### Kết cấu Sân Giếng Bảo Vệ Vệ Sinh Đầu Giếng (Sanitary Apron Protection - Figure fig_ch02_007)
Nhược điểm chí mạng của giếng nông là nguy cơ nhiễm khuẩn Coliform và Nitrat từ nước thải sinh hoạt thấm từ bề mặt đất xuống. Tiêu chuẩn vệ sinh yêu cầu:
- **Sân phơi bê tông (Concrete Apron)**: Đổ sàn bê tông cốt thép nguyên khối bán kính $R \ge 1.5 - 2.0\text{ m}$ xung quanh miệng giếng, độ dốc nghiêng ra ngoài $i = 2\% - 3\%$.
- **Thành giếng nhô cao**: Miệng ống vách phải xây nhô cao hơn mặt sân tối thiểu $0.8\text{ m}$ để ngăn gia súc và nước mưa chảy tràn.
- **Mương thoát nước vòng ngoài**: Dẫn nước rửa và nước tràn chảy xa khỏi miệng giếng tối thiểu $5 - 10\text{ m}$ vào hố thấm riêng biệt.
- **Trám kín vách tầng mặt**: Khoảng không gian hình xuyến sau lưng ống vách bê tông ở độ sâu $3.0\text{ m}$ trên cùng phải được lèn chặt bằng đất sét sét dẻo (puddle clay) hoặc trám vữa xi măng để cắt đứt đường thấm tắt của vi khuẩn từ mặt đất.

---

#### 2.3.2 Giếng Đóng / Giếng Xăm (Driven Wells / Well Points)
##### 2.3.2.1 Cấu tạo Mũi Giếng Đóng và Ống Lưới (Drive Point & Perforated Screen Anatomy - Figure fig_ch02_006)
- Thông số: **Driven Well (Well Point) Galvanized Pipe Diameter** (`dp_ch02_013`):
  $$D_{\text{driven\_well}} = 32 - 50\text{ mm} \quad (1.25 - 2.0\text{ inches})$$
- Thông số: **Driven Well Typical Depth Limit** (`dp_ch02_014`):
  $$H_{\text{driven\_well}} = 5 - 12\text{ m}$$
- **Mũi xuyên (Drive Point / Well Point)**: Chế tạo bằng thép rèn đặc hoặc gang đúc hình chóp nón nhọn gắn ở đầu dưới cùng để xuyên thủng các lớp đất cát.
- **Đoạn ống thu nước có lưới**: Nằm ngay trên mũi nhọn, gồm đoạn ống thép khoan lỗ đục hoa mai bọc ngoài bằng lớp lưới đồng hoặc thép không gỉ (mắt lưới $0.25 - 0.5\text{ mm}$) để ngăn cát hạt trung và hạt mịn lọt vào. Phía trên nối dài bằng các đoạn ống thép mạ kẽm ren bước ốc dài $1.5 - 2.0\text{ m}$.

##### 2.3.2.2 Phương pháp Lắp Đặt và Giới Hạn Thủy Lực
- **Lắp đặt**: Dùng tạ nặng hoặc búa máy đóng trực tiếp ống xuống đất mà không cần khoan tạo lỗ trước. Phương pháp này thi công cực nhanh, giá thành rẻ, nhưng chỉ áp dụng được trong địa tầng đất cát mềm bở rời, không có sỏi cuội lớn hoặc đá tảng.
- **Giới hạn thủy lực**: Do đường kính ống rất nhỏ ($32 - 50\text{ mm}$), không thể thả bơm chìm xuống giếng. Do đó giếng đóng bắt buộc phải khai thác bằng máy bơm ly tâm đặt cạn trên mặt đất hoặc bơm tay pit-tông. Điều này giới hạn chiều sâu mực nước tĩnh và mực nước động không được sâu quá **$6.0 - 7.5\text{ m}$** tính từ mặt đất (do giới hạn hút chân không khí quyển).

---

#### 2.3.3 Thủy Lực Dòng Chảy Hướng Tâm vào Giếng Tầng Không Áp (Unconfined Aquifer Hydraulics)
##### 2.3.3.1 Giả thuyết Dupuit-Forchheimer và Đạo hàm Dòng Thấm (Dupuit Assumptions)
Dòng chảy ngầm hướng tâm vào một giếng khoan hoặc giếng đào hoàn chỉnh trong tầng chứa nước không áp (Unconfined / Phreatic Aquifer) có bề mặt nước tự do bị uốn cong (Free water table phreatic surface). Để giải tích toán học, nhà công binh người Pháp Jules Dupuit (1863) đã đề xuất các giả thuyết thủy lực nền tảng:
1. Độ dốc thủy lực của mặt nước ngầm xấp xỉ bằng tiếp tuyến góc nghiêng mặt tự do: $i = \frac{dh}{dr}$.
2. Các đường đẳng thế thủy đầu (equipotential surfaces) là các mặt trụ đứng đồng tâm với tim giếng.
3. Vận tốc dòng thấm chủ yếu theo phương nằm ngang ($v_r$), vận tốc theo phương thẳng đứng ($v_z$) bị triệt tiêu bỏ qua.

Theo định luật Darcy, lưu lượng thấm hướng tâm $Q$ qua một mặt trụ hở bán kính $r$ có chiều cao $h$ được thiết lập:

$$Q = v \cdot A = K \cdot i \cdot A = K \cdot \left(\frac{dh}{dr}\right) \cdot (2\pi r h)$$

Tách biến số vi phân:

$$Q \cdot \frac{dr}{r} = 2\pi K \cdot h \, dh$$

Tích phân hai vế từ bán kính giếng $r_w$ (nơi có cột nước động $h_w$) đến bán kính ảnh hưởng ngoài $R$ (nơi mực nước không đổi $H_0$):

$$Q \int_{r_w}^{R} \frac{dr}{r} = 2\pi K \int_{h_w}^{H_0} h \, dh \implies Q \cdot \ln\left(\frac{R}{r_w}\right) = 2\pi K \left[ \frac{H_0^2 - h_w^2}{2} \right]$$

##### 2.3.3.2 Phương trình Dupuit-Thiem cho Giếng Tầng Không Áp (Dupuit-Thiem Equation)
Phương trình xác định lưu lượng hoặc cao độ mặt nước ngầm tại hai điểm quan trắc bất kỳ ở khoảng cách $r_1$ và $r_2$:

$$\text{Phương trình Dupuit-Thiem: } Q = \frac{\pi K (h_2^2 - h_1^2)}{\ln(r_2 / r_1)}$$

- **Mã phương trình**: `eq_ch02_002`
- **Ý nghĩa các biến số**:
  - $Q$: Lưu lượng khai thác ổn định từ giếng không áp ($\text{m}^3/\text{s}$ hoặc $\text{m}^3/\text{ngày}$).
  - $K$: Hệ số thấm của tầng chứa nước cát không áp ($\text{m/s}$ hoặc $\text{m/ngày}$).
  - $h_1, h_2$: Chiều cao cột nước bão hòa đo từ đáy cách nước lên mặt tự do tại khoảng cách bán kính $r_1$ và $r_2$ ($\text{m}$).
  - $r_1, r_2$: Khoảng cách xuyên tâm từ tim giếng bơm đến các giếng quan trắc ($r_2 > r_1$) ($\text{m}$).

Khi áp dụng giữa vách giếng khoan ($r_1 = r_w$, $h_1 = h_w$) và biên bán kính ảnh hưởng ngoài ($r_2 = R$, $h_2 = H_0$):

$$Q = \frac{\pi K (H_0^2 - h_w^2)}{\ln(R / r_w)} \iff h_w = \sqrt{H_0^2 - \frac{Q \cdot \ln(R / r_w)}{\pi K}}$$

Độ hạ mực nước tại giếng được xác định: $s_w = H_0 - h_w$. Trong thực tế kỹ thuật, độ hạ mực nước an toàn của giếng tầng không áp không được vượt quá $50\%$ chiều dày bão hòa ban đầu ($s_w \le 0.5 \cdot H_0$) để tránh hiện tượng sụt giảm đột ngột lưu lượng và cuốn cát vào giếng.

##### 2.3.3.3 Bài Tập Tính Toán Điển Hình Giếng Nước Nông Tầng Không Áp (Worked Example EX-CH02-02)
###### Đề bài (Problem Statement)
Một tầng chứa nước cát hạt trung không áp có chiều dày bão hòa ban đầu $H_0 = 18.0\text{ m}$ nằm trên một tầng sét cách nước nằm ngang. Hệ số thấm của tầng cát được xác định qua thí nghiệm hiện trường là $K = 15.0\text{ m/ngày}$.
Một giếng khai thác hoàn chỉnh có bán kính ống vách $r_w = 0.25\text{ m}$ được bơm hút liên tục với lưu lượng ổn định $Q = 864\text{ m}^3/\text{ngày}$ ($10.0\text{ L/s}$). Bán kính ảnh hưởng ngoài của phễu hạ mực nước nơi độ hạ mực nước xấp xỉ bằng $0$ là $R = 250.0\text{ m}$.
Hãy tính toán:
1. Chiều cao cột nước động bão hòa $h_w$ tại vách giếng và độ hạ mực nước tại giếng $s_w$.
2. Chiều cao cột nước $h_1$ và độ hạ mực nước $s_1$ tại một giếng quan trắc nằm cách tim giếng bơm một khoảng $r_1 = 25.0\text{ m}$.
3. Đánh giá tỷ lệ phần trăm độ hạ mực nước tại giếng so với chiều dày tầng chứa nước ban đầu và kiểm tra điều kiện khai thác an toàn.

###### Thông số cho trước (Given Data)
- Chiều dày bão hòa ban đầu $H_0 = 18.0\text{ m}$.
- Hệ số thấm $K = 15.0\text{ m/ngày}$.
- Lưu lượng bơm hút $Q = 864.0\text{ m}^3/\text{ngày}$.
- Bán kính giếng $r_w = 0.25\text{ m}$.
- Bán kính ảnh hưởng $R = 250.0\text{ m}$.
- Bán kính quan trắc $r_1 = 25.0\text{ m}$.

###### Lời giải Chi tiết Từng bước (Step-by-Step Solution)
- **Bước 1: Tính chiều cao nước động $h_w$ và độ hạ mực nước $s_w$ tại giếng**:
  - Áp dụng công thức Dupuit-Thiem biến đổi:
    $$h_w^2 = H_0^2 - \frac{Q \cdot \ln(R / r_w)}{\pi K}$$
  - Tính logarit tỷ số bán kính:
    $$\frac{R}{r_w} = \frac{250.0}{0.25} = 1000 \implies \ln(1000) = 6.907755$$
  - Bình phương chiều dày ban đầu:
    $$H_0^2 = 18.0^2 = 324.0\text{ m}^2$$
  - Tính toán số hạng suy giảm:
    $$\frac{Q \cdot \ln(R / r_w)}{\pi K} = \frac{864.0 \times 6.907755}{\pi \times 15.0} = \frac{5968.300}{47.12389} = 126.651\text{ m}^2$$
  - Tính $h_w^2$ và $h_w$:
    $$h_w^2 = 324.0 - 126.651 = 197.349\text{ m}^2 \implies h_w = \sqrt{197.349} = 14.048\text{ m}$$
  - Độ hạ mực nước tại vách giếng:
    $$s_w = H_0 - h_w = 18.0 - 14.048 = 3.952\text{ m}$$

- **Bước 2: Tính mực nước $h_1$ và độ hạ mực nước $s_1$ tại điểm cách giếng $r_1 = 25.0\text{ m}$**:
  - Tỷ số bán kính:
    $$\frac{R}{r_1} = \frac{250.0}{25.0} = 10 \implies \ln(10) = 2.302585$$
  - Tính $h_1^2$:
    $$h_1^2 = H_0^2 - \frac{Q \cdot \ln(R / r_1)}{\pi K} = 324.0 - \frac{864.0 \times 2.302585}{47.12389} = 324.0 - 42.217 = 281.783\text{ m}^2$$
  - Mực nước bão hòa:
    $$h_1 = \sqrt{281.783} = 16.786\text{ m}$$
  - Độ hạ mực nước tại khoảng cách $25\text{ m}$:
    $$s_1 = H_0 - h_1 = 18.0 - 16.786 = 1.214\text{ m}$$

- **Bước 3: Đánh giá tỷ lệ phần trăm độ hạ mực nước**:
  - Tỷ lệ độ hạ mực nước tại vách giếng:
    $$\frac{s_w}{H_0} \times 100\% = \frac{3.952}{18.0} \times 100\% = 21.96\% \approx 21.94\%$$
  - *Kết luận*: Do $s_w / H_0 = 21.96\% < 50\%$, chế độ hạ mực nước nằm trong giới hạn an toàn tối ưu của tầng chứa nước không áp, không gây cạn kiệt cục bộ và ngăn ngừa sụt lở tầng cát xung quanh giếng.

###### Đáp số (Final Answer)
- Mực nước động tại giếng $h_w = 14.05\text{ m}$; Độ hạ mực nước tại giếng $s_w = 3.95\text{ m}$.
- Mực nước tại vị trí $25\text{ m}$: $h_1 = 16.79\text{ m}$; Độ hạ mực nước $s_1 = 1.21\text{ m}$.
- Tỷ lệ hạ mực nước: $21.94\%$ ($< 50\%$, đạt tiêu chuẩn khai thác an toàn bền vững).

---

#### 2.3.4 Hành Lang Thu Nước Thấm Ven Sông và Lọc Ven Bờ (Alluvial Infiltration Galleries & Riverbank Filtration - RBF)
##### 2.3.4.1 Cơ Chế Lọc Tự Nhiên Ven Sông (Riverbank Filtration Natural Attenuation Mechanisms)
Hành lang thu nước thấm ven sông (Infiltration Gallery) và giếng thu tia nan hoa Ranney khai thác công nghệ lọc bờ sông tự nhiên (Riverbank Filtration - RBF). Khi bơm hút nước từ các công trình thu ngầm đặt trong dải cát cuội alluvium ven sông, nước sông sẽ thấm qua lớp trầm tích đáy và thân đê bãi bồi để vào công trình:
- **Hiệu quả xử lý tự nhiên tuyệt vời**:
  1. *Lắng và lọc cơ học*: Giữ lại $99\% - 99.9\%$ độ đục và cặn lơ lửng, nước thấm thu được có độ đục thường xuyên $< 1\text{ NTU}$ ngay cả trong mùa lũ đục ngầu phù sa.
  2. *Hấp phụ và trao đổi ion*: Giữ lại các chất hữu cơ tự nhiên ($\text{NOM}$), dầu mỡ và kim loại nặng trên bề mặt hạt khoáng sét và oxit sắt-mangan.
  3. *Phân hủy sinh học (Biological Degradation)*: Lớp màng vi sinh vật bám dính (biofilm) trong tầng đất cát phân hủy các chất ô nhiễm vi lượng hữu cơ, dược phẩm và thuốc trừ sâu.
  4. *Loại bỏ vi sinh vật mầm bệnh*: Tiêu diệt và loại bỏ hiệu quả các nang kén đơn bào kháng clo như *Giardia lamblia* ($> 3 - 4\text{ log}$) và *Cryptosporidium oocysts* ($> 4\text{ log}$), giảm thiểu rủi ro bùng phát dịch bệnh tiêu chảy cấp.

##### 2.3.4.2 Thủy Lực và Cấu Tạo Hành Lang Thu Nước Thấm Tuyến Tính (Infiltration Gallery Engineering)
###### Cấu Tạo Rãnh Thu Thấm
Một hành lang thu nước thấm gồm đường rãnh đào sâu song song với bờ sông, đặt dưới cao trình mực nước kiệt của sông:
- **Đường ống thu đục lỗ (Perforated Collector Pipe)**: Chế tạo bằng bê tông đục lỗ, ống gang dẻo có khe hoặc ống nhựa gân HDPE/PVC xẻ rãnh (đường kính $\text{DN}200 - \text{DN}500$). 
- Thông số: **Infiltration Gallery Perforated Collector Pipe Flow Velocity** (`dp_ch02_020`):
  $$v_{\text{gallery\_pipe}} = 0.50 - 1.00\text{ m/s}$$
  *Mục đích*: Vận tốc $\ge 0.5\text{ m/s}$ chống lắng cặn mịn chui vào ống, và $\le 1.0\text{ m/s}$ hạn chế ma sát thủy lực.
- **Tầng sỏi lọc bao bọc (Graded Gravel Pack Envelopes)**: Xung quanh ống thu được bọc tối thiểu 2 đến 3 lớp sỏi lọc ngược có kích thước hạt tăng dần từ ngoài vào trong để ngăn cát sông chui vào ống gây nghẹt. Toàn bộ rãnh được lót vải địa kỹ thuật không dệt (geotextile) chống xáo trộn địa tầng.
- **Giếng tập trung nước (Collection Sump)**: Nước từ đường ống dẫn tự chảy về hố ga bê tông kín đặt máy bơm chuyển tiếp lên trạm xử lý.

###### Phương trình Thủy lực Thấm Dừng Thu Nước Ven Sông (Infiltration Gallery Yield Equation)
Lưu lượng nước thấm dừng một chiều từ dòng sông vào hành lang thu đặt song song cách bờ sông khoảng cách $L_{\text{distance}}$ được xác định theo mô hình thấm Dupuit:

$$\text{Lưu lượng hành lang thấm: } Q = K \cdot L_{\text{gallery}} \cdot \frac{H^2 - h_0^2}{2 L_{\text{distance}}}$$

- **Mã phương trình**: `eq_ch02_012`
- **Ý nghĩa các biến số**:
  - $Q$: Lưu lượng nước thu hoạch được của hành lang thấm ($\text{m}^3/\text{s}$ hoặc $\text{m}^3/\text{ngày}$).
  - $K$: Hệ số thấm ngang của tầng phù sa cát sỏi alluvium ven sông ($\text{m/s}$ hoặc $\text{m/ngày}$).
  - $L_{\text{gallery}}$: Tổng chiều dài hoạt động của tuyến ống thu đục lỗ đặt ngầm ($\text{m}$).
  - $H$: Chiều cao cột nước của sông tính từ đáy cách nước nằm ngang lên mặt nước sông ($\text{m}$).
  - $h_0$: Chiều cao cột nước bên trong tuyến ống thu thấm tính từ đáy cách nước ($\text{m}$).
  - $L_{\text{distance}}$: Khoảng cách vuông góc từ mép nước bờ sông đến tim tuyến hành lang thu ($\text{m}$).
  - Năng suất thu nước trên một mét dài hành lang: $q = Q / L_{\text{gallery}} = K \cdot \frac{H^2 - h_0^2}{2 L_{\text{distance}}}$ ($\text{m}^3/(\text{ngày}\cdot\text{m})$).

##### 2.3.4.3 Giếng Thu Nước Hướng Tâm Kiểu Ranney (Ranney Radial Collector Wells)
Đối với các nhà máy nước công suất lớn đặt ven các con sông lớn phù sa, công trình thu nước kiểu Ranney là giải pháp công nghệ đỉnh cao:
- **Cấu tạo**: Một giếng chìm trung tâm bằng bê tông cốt thép đường kính rất lớn ($D = 4.0 - 6.0\text{ m}$), thành dày $0.5 - 0.8\text{ m}$ hạ sâu tới tầng cát sỏi đáy.
- **Ống lọc nan hoa ngang (Lateral perforated screens)**: Từ đáy giếng chìm, sử dụng kích thủy lực công suất lớn kích các đường ống thép không gỉ xẻ khe liên tục đẩy xuyên ngang tỏa ra như các nan hoa xe đạp đâm sâu vào tầng bão hòa alluvium dưới lòng sông (chiều dài mỗi nan hoa $30 - 80\text{ m}$, số lượng từ $4$ đến $12$ nan).
- **Ưu điểm**: Thu gom lưu lượng khổng lồ ($20,000 - 100,000\text{ m}^3/\text{ngày}$) chỉ trên một diện tích mặt bằng trạm bơm cực nhỏ, chất lượng nước sạch trong vắt không cần qua công đoạn keo tụ - lắng mà chỉ cần khử trùng clo là đạt chuẩn nước sinh hoạt.

##### 2.3.4.4 Bài Tập Tính Toán Điển Hình Hành Lang Thu Nước Thấm (Worked Example EX-CH02-08)
###### Đề bài (Problem Statement)
Thiết kế một hành lang thu nước thấm ven sông (hệ thống lọc bờ sông RBF) đặt trong tầng phù sa cát sỏi bãi bồi không áp.
Mặt nước sông duy trì cột nước bão hòa ổn định $H = 9.0\text{ m}$ so với lớp đá nền không thấm nằm ngang. Khoảng cách vuông góc từ mép bờ sông đến tim tuyến hành lang thu là $L_{\text{distance}} = 40.0\text{ m}$. Hệ số thấm của tầng cát sỏi ven sông là $K = 35.0\text{ m/ngày}$ ($4.051 \times 10^{-4}\text{ m/s}$).
Tuyến ống thu nước đục lỗ nằm ngang có chiều dài hoạt động $L_{\text{gallery}} = 60.0\text{ m}$ và duy trì mực nước động rút thấp bên trong ống thu là $h_0 = 5.50\text{ m}$ so với đáy cách nước.
Vận tốc dòng chảy trong đường ống thu gom dẫn về giếng tập trung không được vượt quá vận tốc cho phép $v_{\text{pipe, max}} \le 0.80\text{ m/s}$.
Hãy tính toán:
1. Lưu lượng nước thô ổn định $Q$ thu được từ hành lang thu nước thấm ($\text{m}^3/\text{ngày}$ và $\text{L/s}$).
2. Năng suất thu nước đơn vị $q$ trên một mét dài của tuyến hành lang thu ($\text{m}^3/(\text{ngày}\cdot\text{m})$).
3. Đường kính trong danh định tối thiểu của đường ống thu nước đục lỗ ($D_{\text{pipe}}$) và lựa chọn kích thước ống thương phẩm theo tiêu chuẩn.

###### Thông số cho trước (Given Data)
- Cột nước sông $H = 9.0\text{ m}$.
- Cột nước trong ống thu $h_0 = 5.5\text{ m}$.
- Khoảng cách đến sông $L_{\text{distance}} = 40.0\text{ m}$.
- Hệ số thấm $K = 35.0\text{ m/ngày}$.
- Chiều dài tuyến ống thu $L_{\text{gallery}} = 60.0\text{ m}$.
- Vận tốc tối đa trong ống $v_{\text{pipe, max}} = 0.80\text{ m/s}$.

###### Lời giải Chi tiết Từng bước (Step-by-Step Solution)
- **Bước 1: Tính lưu lượng khai thác của hành lang thấm**:
  - Áp dụng công thức dòng thấm dừng Dupuit cho hành lang ven sông (`eq_ch02_012`):
    $$Q = K \cdot L_{\text{gallery}} \cdot \frac{H^2 - h_0^2}{2 L_{\text{distance}}}$$
  - Tính toán các số hạng cột nước:
    $$H^2 - h_0^2 = 9.0^2 - 5.5^2 = 81.0 - 30.25 = 50.75\text{ m}^2$$
    $$2 L_{\text{distance}} = 2 \times 40.0 = 80.0\text{ m}$$
    $$\frac{H^2 - h_0^2}{2 L_{\text{distance}}} = \frac{50.75}{80.0} = 0.634375$$
  - Tính lưu lượng ngày:
    $$Q = 35.0 \times 60.0 \times 0.634375 = 2100.0 \times 0.634375 = 1,332.1875\text{ m}^3/\text{ngày}$$
  - Đổi đơn vị sang $\text{m}^3/\text{s}$ và $\text{L/s}$:
    $$Q = \frac{1332.1875}{86,400} = 0.015419\text{ m}^3/\text{s} \approx 15.42\text{ L/s}$$

- **Bước 2: Tính năng suất thu nước đơn vị trên một mét dài**:
  $$q = \frac{Q}{L_{\text{gallery}}} = \frac{1332.1875}{60.0} = 22.203\text{ m}^3/(\text{ngày}\cdot\text{m})$$

- **Bước 3: Định cỡ đường kính trong ống thu gom nước**:
  - Diện tích mặt cắt ướt tối thiểu của ống thu gom để lưu thông toàn bộ lưu lượng $Q$ ở cuối tuyến:
    $$A_{\text{pipe}} = \frac{Q}{v_{\text{pipe, max}}} = \frac{0.015419}{0.80} = 0.019274\text{ m}^2$$
  - Tính đường kính trong tối thiểu:
    $$D_{\text{pipe}} = \sqrt{\frac{4 \cdot A_{\text{pipe}}}{\pi}} = \sqrt{\frac{4 \times 0.019274}{\pi}} = \sqrt{0.024540} = 0.15665\text{ m} \approx 156.7\text{ mm}$$
  - Chọn đường kính ống thương phẩm tiêu chuẩn: **DN200** (đường kính trong danh nghĩa $D = 200\text{ mm} = 0.20\text{ m}$).
  - Kiểm tra vận tốc thực tế trong ống $\text{DN}200$:
    $$v_{\text{actual}} = \frac{Q}{\pi \times D^2 / 4} = \frac{0.015419}{\pi \times (0.20)^2 / 4} = \frac{0.015419}{0.031416} = 0.491\text{ m/s}$$
  - *Đánh giá*: Vận tốc thực tế $v_{\text{actual}} = 0.491\text{ m/s} \approx 0.50\text{ m/s} \le 0.80\text{ m/s}$, vừa đủ tự làm sạch cuốn trôi cặn hạt mịn và không gây tổn thất thủy lực quá mức, đạt tiêu chuẩn thiết kế.

###### Đáp số (Final Answer)
- Lưu lượng thu hoạch $Q = 1,332.19\text{ m}^3/\text{ngày}$ ($15.42\text{ L/s}$).
- Năng suất đơn vị $q = 22.20\text{ m}^3/(\text{ngày}\cdot\text{m})$.
- Đường kính trong tối thiểu $D = 156.7\text{ mm}$ (lựa chọn ống tiêu chuẩn **DN200** với vận tốc thực tế $0.49\text{ m/s} \le 0.80\text{ m/s}$, đạt yêu cầu).

---

### 2.4 Công Trình Thu Nước Ngầm Tầng Sâu: Cấu Tạo và Thủy Lực Giếng Khoan (Deep Drilled Production Wells & Well Hydraulics)
#### 2.4.1 Cấu Tạo Cơ Khí Giếng Khoan Công Nghiệp (Deep Drilled Well Mechanical Anatomy)
##### 2.4.1.1 Mặt Cắt Địa Chất - Cơ Khí Tổng Thể Giếng Khoan Tầng Sâu (Figure fig_ch02_009)
Giếng khoan công nghiệp khai thác tầng chứa nước có áp (Confined Aquifer) là một cấu trúc địa kỹ thuật phức tạp đòi hỏi độ chính xác cơ học và vệ sinh tuyệt đối:
```
Mặt đất tự nhiên (Ground Surface)
  |===|  Miệng giếng & Nắp bảo vệ (Wellhead & Sanitary Cap)
  |   |  Sân bê tông bảo vệ bán kính 1.5 - 2.0 m
  | G |  Ống chống bề mặt (Surface Casing)
  | R |  Vữa xi măng trám áp lực cao (Sanitary Cement Grout Seal >= 5-10 m)
  | O |
  | U |====================================================== Tầng cách nước trên (Upper Confining Bed)
  | T |  Ống vách khai thác (Production Casing D = 150 - 400 mm)
  |   |
  |===|  Vị trí đặt Bơm chìm (Submersible Pump) [d_clearance >= 50 mm]
  |   |  Mực nước động (Dynamic Pumping Water Level - PWL)
  |---|====================================================== Đỉnh tầng chứa nước (Top of Aquifer)
  | S |  Ống lọc khe quấn Johnson (Continuous-Slot Johnson Screen)
  | C |  Chèn sỏi lọc silica nhân tạo (Graded Siliceous Gravel Pack 75-150 mm)
  | R |  Tầng chứa nước có áp (Confined Sand/Gravel Aquifer, Bề dày B)
  | E |
  | E |
  | N |====================================================== Đáy tầng chứa nước (Bottom of Aquifer)
  | T |  Ống lắng bùn cát (Sand Trap / Sediment Sump Pipe dài 3 - 6 m)
  |===|  Nắp đáy kín hàn chặt (Welded Bottom Plug)
```

##### 2.4.1.2 Ống Chống Bề Mặt và Bơm Trám Vữa Xi Măng Cách Ly Vệ Sinh (Surface Casing & Sanitary Grout)
- Thông số: **Deep Well Sanitary Surface Grout Seal Minimum Depth** (`dp_ch02_009`):
  $$z_{\text{sanitary\_seal}} \ge 5 - 10\text{ m} \quad (\text{tiêu chuẩn công nghiệp: } 10 - 15\text{ m})$$
- **Kỹ thuật trám vữa áp lực (Pressure Grouting)**: Khoảng không gian hình xuyến giữa thành vách lỗ khoan đất đá và ống chống bề mặt (annular space) bắt buộc phải được bơm lấp đầy từ dưới đáy ngược lên bằng vữa xi măng nguyên chất (neat cement slurry) trộn $2\% - 5\%$ bentonite chống co ngót dưới áp lực cao.
- **Ý nghĩa sống còn**:
  1. Tạo lớp niêm phong cơ học vĩnh cửu ngăn chặn triệt để nước mặt, nước thải và hóa chất độc hại từ mặt đất thấm dọc theo vách giếng chui xuống tầng ngầm sâu.
  2. Cách ly các tầng chứa nước lợ/mặn phía trên, bảo vệ tầng nước ngọt sâu bên dưới không bị nhiễm bẩn chéo.
  3. Cố định vững chắc ống vách giếng chống rung lắc do hoạt động của máy bơm công suất lớn.

##### 2.4.1.3 Ống Vách Khai Thác và Khoảng Hở Thủy Lực Lắp Đặt Bơm (Production Casing & Clearance)
- **Đường kính ống vách khai thác**: Dao động từ $\text{DN}150 - \text{DN}400$ ($6 - 16\text{ inches}$) bằng thép carbon chịu lực hoặc nhựa uPVC dày chịu áp lực.
- Thông số: **Deep Production Well Minimum Casing Clearance over Submersible Pump** (`dp_ch02_010`):
  $$d_{\text{clearance}} \ge 50\text{ mm}$$
- **Cơ sở thủy động lực**: Đường kính trong của ống vách phải lớn hơn đường kính ngoài của cụm bơm chìm tối thiểu $50\text{ mm}$ (tiêu chuẩn khuyến cáo chênh lệch kích thước tối thiểu $2\text{ inches} = 50.8\text{ mm}$). Khoảng hở hình xuyến này bảo đảm vận tốc dòng nước đi ngược từ ống lọc lên qua bề mặt vỏ động cơ điện đạt giá trị tối ưu ($0.15 - 0.90\text{ m/s}$), giải nhiệt làm mát cưỡng bức cuộn dây stato động cơ, ngăn ngừa cháy bơm do quá nhiệt.

##### 2.4.1.4 Ống Lọc Khe Quấn Dây Johnson Liên Tục (Continuous-Slot Wire-Wrapped Johnson Screens)
###### Hình Dạng Hình Học Dây Nêm V-Wire và Cơ Chế Tự Làm Sạch Chống Nghẹt (Figure fig_ch02_010)
Ống lọc giếng khoan Johnson là phát minh mang tính cách mạng trong ngành kỹ thuật nước ngầm:
- **Tiết diện dây quấn hình nêm (V-shaped wire profile)**: Dây thép không gỉ được kéo thành hình tam giác/hình nêm và hàn điện điện trở nóng chảy liên tục lên các thanh giằng dọc (vertical support rods).
- **Mặt khe mở rộng vào trong**: Đỉnh nhọn của dây V quay ra ngoài tiếp xúc với cát, hai cạnh vát mở rộng dần vào trong lòng ống. Nếu một hạt cát đi lọt qua khe mặt ngoài, nó sẽ lọt thẳng vào trong lòng ống mà không bao giờ bị kẹt lại ở giữa khe. Cấu tạo này giúp ống lọc Johnson có khả năng **tự làm sạch chống nghẹt tuyệt đối (non-clogging)** so với ống xẻ rãnh thủ công hoặc đục lỗ thông thường (rất dễ bị hạt cát nêm chặt làm tắc nghẽn vĩnh viễn).

###### Tỷ Lệ Diện Tích Mở Thông Thủy Lưới Johnson
- Thông số: **Continuous-Slot Wire-Wrapped Well Screen Fractional Open Area** (`dp_ch02_007`):
  $$C_{\text{open}} = 15 - 30\% \quad (\text{đạt tới } 40\% \text{ đối với cỡ khe lớn})$$
- *So sánh*: Ống thép đục lỗ hoặc xẻ rãnh cưa chỉ đạt tỷ lệ mở $3\% - 5\%$. Diện tích mở lớn của lưới Johnson giúp giảm tổn thất ma sát cục bộ qua khe xuống mức cực vi mô, tiết kiệm năng lượng điện bơm và hạn chế tối đa độ hạ mực nước động.

###### Tiêu Chuẩn Lựa Chọn Cỡ Khe Lọc Dựa trên Đường Cong Cấp Phối Hạt
Kích thước khe hở ống lọc (Slot size, tính bằng $1/1000\text{ inch}$ hoặc $\text{mm}$) được quyết định chính xác dựa trên đường cong thành phần hạt thí nghiệm rây (Sieve analysis):
- Khi **không chèn sỏi** (tầng cát thô đồng nhất): Chọn cỡ khe giữ lại $40\% - 50\%$ khối lượng mẫu đất ($D_{40} - D_{50}$).
- Khi **có chèn sỏi lọc nhân tạo** (tầng cát mịn, không đồng nhất): Chọn cỡ khe giữ lại tối thiểu $90\% - 95\%$ khối lượng của lớp sỏi lọc nhân tạo chèn xung quanh ống lọc ($d_{\text{slot}} = D_{10\text{ of gravel}}$).

##### 2.4.1.5 Tầng Sỏi Lọc Nhân Tạo và Ống Lắng Cát Đáy Giếng (Artificial Gravel Pack & Sand Trap)
- Thông số: **Artificial Siliceous Gravel Pack Envelope Thickness** (`dp_ch02_008`):
  $$t_{\text{gravel\_pack}} = 75 - 150\text{ mm} \quad (3 - 6\text{ inches})$$
- **Yêu cầu vật liệu sỏi lọc**: Phải là sỏi thạch anh (siliceous gravel) tròn cạnh, độ mài mòn thấp, thành phần $\text{SiO}_2 > 95\%$, hàm lượng đá vôi $\text{CaCO}_3 < 5\%$ để không bị hòa tan bởi axit trong quá trình súc rửa giếng. Tỷ lệ đồng nhất $U_c = d_{60}/d_{10} < 2.5$.
- **Tỷ lệ cấp phối sỏi-tầng chứa (Pack-to-Aquifer Ratio)**: Kích thước $d_{50}$ của sỏi lọc thường gấp $4$ đến $6$ lần kích thước $D_{50}$ của cát tầng chứa nước ($d_{50,\text{pack}} = (4 - 6) \cdot D_{50,\text{aquifer}}$).
- **Ống lắng cát đáy giếng (Sand Trap Sump)**: Nằm dưới cùng của giếng, chế tạo bằng đoạn ống vách kín đáy dài $3 - 6\text{ m}$. Đóng vai trò là hố gom lắng đọng cát mịn lọt vào giếng trong giai đoạn thổi rửa ban đầu, ngăn không cho cát dâng cao làm nghẹt bề mặt ống lọc.

---

#### 2.4.2 Thủy Lực Dòng Chảy Hướng Tâm Tầng Có Áp (Confined Aquifer Steady-State Well Hydraulics)
##### 2.4.2.1 Thiết Lập Định Luật Darcy và Phương Trình Thiem (Darcy's Law & Thiem Equation Derivation)
Xét một giếng khoan hoàn chỉnh khoan xuyên qua toàn bộ bề dày $B$ của một tầng chứa nước có áp nằm giữa hai tầng sét cách nước tuyệt đối:
- Chiều dày bão hòa của tầng chứa nước là hằng số $B = \text{const}$.
- Dòng chảy thấm ngầm hướng tâm hoàn toàn theo phương ngang.

Áp dụng định luật Darcy, lưu lượng thấm $Q$ qua diện tích xung quanh hình trụ bán kính $r$ có chiều cao $B$:

$$Q = v \cdot A = K \cdot \left(\frac{dh}{dr}\right) \cdot (2\pi r B) = 2\pi K B \cdot r \cdot \frac{dh}{dr}$$

Định nghĩa hệ số dẫn nước (Transmissivity $T$):

$$T = K \cdot B \quad (\text{đơn vị: } \text{m}^2/\text{s} \text{ hoặc } \text{m}^2/\text{ngày})$$

Thay $T$ vào phương trình và tách biến số vi phân:

$$Q \cdot \frac{dr}{r} = 2\pi T \, dh$$

Tích phân hai vế giữa hai giếng quan trắc ở khoảng cách $r_1$ và $r_2$ (tương ứng với cột nước áp lực $h_1$ và $h_2$, hoặc độ hạ mực nước $s_1 = H_0 - h_1$ và $s_2 = H_0 - h_2$):

$$Q \int_{r_1}^{r_2} \frac{dr}{r} = 2\pi T \int_{h_1}^{h_2} dh \implies Q \cdot \ln\left(\frac{r_2}{r_1}\right) = 2\pi T (h_2 - h_1) = 2\pi T (s_1 - s_2)$$

##### 2.4.2.2 Phương Trình Thiem Toàn Diện (Thiem Equation)
Phương trình Thiem tính lưu lượng dòng thấm dừng hướng tâm vào giếng có áp:

$$\text{Phương trình Thiem: } Q = \frac{2\pi K B (h_2 - h_1)}{\ln(r_2 / r_1)} = \frac{2\pi T (s_1 - s_2)}{\ln(r_2 / r_1)}$$

- **Mã phương trình**: `eq_ch02_001`
- **Ý nghĩa các biến số**:
  - $Q$: Lưu lượng bơm hút ổn định từ giếng có áp ($\text{m}^3/\text{s}$ hoặc $\text{m}^3/\text{ngày}$).
  - $K$: Hệ số thấm của tầng có áp ($\text{m/s}$ hoặc $\text{m/ngày}$).
  - $B$: Bề dày bão hòa của tầng chứa nước có áp ($\text{m}$).
  - $T$: Hệ số dẫn nước của tầng ($T = K \cdot B$, $\text{m}^2/\text{s}$ hoặc $\text{m}^2/\text{ngày}$).
  - $h_1, h_2$: Cột nước đo áp piezometric tại các giếng quan trắc ở cự ly $r_1$ và $r_2$ ($\text{m}$).
  - $s_1, s_2$: Độ hạ mực nước đo áp tương ứng tại các khoảng cách $r_1$ và $r_2$ ($s = H_0 - h$, $\text{m}$).
  - $r_1, r_2$: Khoảng cách xuyên tâm từ tim giếng bơm đến các giếng quan trắc ($r_2 > r_1$) ($\text{m}$).

Khi nội suy độ hạ mực nước tại vách giếng khoan ($r = r_w$):

$$s_w = s_1 + \frac{Q}{2\pi T} \cdot \ln\left(\frac{r_1}{r_w}\right)$$

##### 2.4.2.3 Bán Kính Ảnh Hưởng Sichardt và Quy Luật Tương Hỗ Giếng (Sichardt Radius & Well Interference)
###### Công thức Kinh nghiệm Sichardt (Sichardt Empirical Formula)
Bán kính ảnh hưởng ngoài $R$ của phễu hạ mực nước (nơi $s = 0$) trong thực tế địa chất rất khó đo lường bằng giếng quan trắc xa. Kỹ thuật thủy văn sử dụng công thức kinh nghiệm Sichardt:

$$\text{Công thức Sichardt: } R = 3000 \cdot s_w \cdot \sqrt{K}$$

- **Mã phương trình**: `eq_ch02_005`
- **Quy ước đơn vị bắt buộc**:
  - $R$: Bán kính ảnh hưởng của phễu hạ mực nước ($\text{m}$).
  - $s_w$: Độ hạ mực nước đo tại vách giếng khoan ($\text{m}$).
  - $K$: Hệ số thấm của tầng chứa nước, **bắt buộc tính bằng mét trên giây ($\text{m/s}$)**.
  - $3000$: Hệ số kinh nghiệm có thứ nguyên.

###### Quy Luật Tương Hỗ Giếng (Well Interference) và Bố Trí Bãi Giếng
- Khi hai hoặc nhiều giếng khoan cùng hoạt động trong một tầng chứa nước, nếu khoảng cách giữa hai giếng nhỏ hơn hai lần bán kính ảnh hưởng ($L < 2R$), phễu hạ mực nước của chúng sẽ giao thoa và xếp chồng lên nhau (drawdown superposition).
- Độ hạ mực nước tổng cộng tại một giếng bất kỳ sẽ tăng thêm một lượng phụ trợ $\Delta s$:
  $$\Delta s_{\text{interference}} = \frac{Q_2}{2\pi T} \cdot \ln\left(\frac{R_2}{L_{1-2}}\right)$$
- Hậu quả: Làm tụt sâu mực nước động bên trong giếng, giảm năng suất giếng, tăng điện năng tiêu thụ và có thể làm cạn kiệt tầng chứa nước cục bộ.
- Thông số: **Inter-Well Separation Distance in Multi-Well Wellfield** (`dp_ch02_019`):
  $$L_{\text{well\_spacing}} \ge (1.5 - 2.0) \cdot R \quad (\text{thông thường từ } 100 - 300\text{ m})$$
  *Quy tắc thiết kế bãi giếng*: Luôn bố trí hàng giếng vuông góc với hướng dòng ngầm tự nhiên để đón lưu lượng bổ cập cực đại.

##### 2.4.2.4 Bài Tập Tính Toán Điển Hình Thử Nghiệm Bơm Tầng Có Áp (Worked Example EX-CH02-01)
###### Đề bài (Problem Statement)
Một giếng khai thác nước ngầm của nhà máy nước đô thị khoan hoàn chỉnh qua một tầng chứa nước cát sỏi có áp có bề dày $B = 24.0\text{ m}$. Giếng được bơm thử nghiệm với lưu lượng khai thác ổn định $Q = 2,400\text{ m}^3/\text{ngày}$ ($27.78\text{ L/s}$).
Số liệu đo đạc độ hạ mực nước ổn định tại hai giếng quan trắc nằm cách tim giếng bơm các khoảng cách lần lượt là $r_1 = 30.0\text{ m}$ và $r_2 = 120.0\text{ m}$ cho kết quả: $s_1 = 3.20\text{ m}$ và $s_2 = 1.45\text{ m}$. Bán kính ống vách của giếng bơm là $r_w = 0.20\text{ m}$ ($200\text{ mm}$).
Hãy tính toán:
1. Hệ số dẫn nước $T$ ($\text{m}^2/\text{ngày}$ và $\text{m}^2/\text{s}$) và hệ số thấm $K$ ($\text{m/ngày}$ và $\text{m/s}$) của tầng chứa nước.
2. Độ hạ mực nước hình thành lý thuyết tại vách giếng khoan ($s_w$).
3. Bán kính ảnh hưởng $R$ của phễu hạ mực nước theo công thức kinh nghiệm Sichardt.

###### Thông số cho trước (Given Data)
- Bề dày tầng chứa nước có áp $B = 24.0\text{ m}$.
- Lưu lượng bơm ổn định $Q = 2400.0\text{ m}^3/\text{ngày}$.
- Khoảng cách giếng quan trắc 1: $r_1 = 30.0\text{ m}$; Độ hạ mực nước $s_1 = 3.20\text{ m}$.
- Khoảng cách giếng quan trắc 2: $r_2 = 120.0\text{ m}$; Độ hạ mực nước $s_2 = 1.45\text{ m}$.
- Bán kính giếng bơm $r_w = 0.20\text{ m}$.

###### Lời giải Chi tiết Từng bước (Step-by-Step Solution)
- **Bước 1: Tính hệ số dẫn nước $T$ theo phương trình Thiem**:
  - Áp dụng công thức Thiem (`eq_ch02_001`):
    $$T = \frac{Q \cdot \ln(r_2 / r_1)}{2\pi (s_1 - s_2)}$$
  - Tỷ số khoảng cách:
    $$\frac{r_2}{r_1} = \frac{120.0}{30.0} = 4.0 \implies \ln(4.0) = 1.386294$$
  - Chênh lệch độ hạ mực nước giữa hai giếng quan trắc:
    $$s_1 - s_2 = 3.20 - 1.45 = 1.75\text{ m}$$
  - Mẫu số:
    $$2\pi \times (s_1 - s_2) = 2 \times \pi \times 1.75 = 10.995574\text{ m}$$
  - Tính hệ số dẫn nước:
    $$T = \frac{2400.0 \times 1.386294}{10.995574} = \frac{3327.106}{10.995574} = 302.586\text{ m}^2/\text{ngày}$$
  - Đổi đơn vị sang $\text{m}^2/\text{s}$:
    $$T = \frac{302.586}{86,400} = 3.50215 \times 10^{-3}\text{ m}^2/\text{s}$$

- **Bước 2: Tính hệ số thấm $K$ của tầng chứa nước**:
  $$K = \frac{T}{B} = \frac{302.586\text{ m}^2/\text{ngày}}{24.0\text{ m}} = 12.6078\text{ m/ngày}$$
  - Đổi sang đơn vị $\text{m/s}$:
    $$K = \frac{12.6078}{86,400} = 1.4592 \times 10^{-4}\text{ m/s}$$

- **Bước 3: Tính độ hạ mực nước lý thuyết tại vách giếng bơm ($r_w = 0.20\text{ m}$)**:
  - Sử dụng số liệu của giếng quan trắc 1 ($r_1 = 30.0\text{ m}$, $s_1 = 3.20\text{ m}$):
    $$s_w = s_1 + \frac{Q}{2\pi T} \cdot \ln\left(\frac{r_1}{r_w}\right)$$
  - Tỷ số khoảng cách:
    $$\frac{r_1}{r_w} = \frac{30.0}{0.20} = 150.0 \implies \ln(150.0) = 5.010635$$
  - Hệ số đứng trước logarit:
    $$\frac{Q}{2\pi T} = \frac{2400.0}{2\pi \times 302.586} = \frac{2400.0}{1901.218} = 1.26235\text{ m}$$
  - Độ hạ mực nước gia tăng từ khoảng cách $30\text{ m}$ vào vách giếng:
    $$\Delta s = 1.26235 \times 5.010635 = 6.3252\text{ m}$$
  - Độ hạ mực nước tổng thể tại vách giếng:
    $$s_w = 3.20 + 6.3252 = 9.5252\text{ m} \approx 9.53\text{ m}$$

- **Bước 4: Tính bán kính ảnh hưởng $R$ theo công thức Sichardt**:
  - Áp dụng công thức Sichardt (`eq_ch02_005`):
    $$R = 3000 \cdot s_w \cdot \sqrt{K}$$
  - Với $K = 1.4592 \times 10^{-4}\text{ m/s}$:
    $$\sqrt{K} = \sqrt{1.4592 \times 10^{-4}} = 0.0120797$$
  - Thay số:
    $$R = 3000 \times 9.5252 \times 0.0120797 = 28,575.6 \times 0.0120797 = 345.18\text{ m} \approx 345.3\text{ m}$$

###### Đáp số (Final Answer)
- Hệ số dẫn nước: $T = 302.59\text{ m}^2/\text{ngày}$ ($3.50 \times 10^{-3}\text{ m}^2/\text{s}$).
- Hệ số thấm: $K = 12.61\text{ m/ngày}$ ($1.46 \times 10^{-4}\text{ m/s}$).
- Độ hạ mực nước lý thuyết tại giếng: $s_w = 9.53\text{ m}$.
- Bán kính ảnh hưởng phễu hạ mực nước: $R = 345.3\text{ m}$.

---

#### 2.4.3 Động Học Độ Hạ Mực Nước, Hiệu Suất Giếng và Năng Suất Riêng (Drawdown Dynamics & Well Performance)
##### 2.4.3.1 Phương Trình Phân Tách Tổn Thất Jacob (Jacob Step-Drawdown Formulation)
Độ hạ mực nước thực tế đo được bên trong ống vách của một giếng đang bơm ($s_w$) luôn lớn hơn độ hạ mực nước lý thuyết của tầng chứa nước. Theo lý thuyết của C.E. Jacob (1947), độ hạ mực nước tổng thể bao gồm hai thành phần vật lý riêng biệt:

$$\text{Tổng độ hạ mực nước: } s_w = H_0 - h_w = s_{\text{aquifer}} + s_{\text{well}} = B_1 Q + C_1 Q^2$$

- **Mã phương trình**: `eq_ch02_003`
- **Ý nghĩa các thành phần**:
  - $s_w$: Tổng độ hạ mực nước đo được trong lòng giếng khoan ($\text{m}$).
  - $H_0$: Mực nước tĩnh trước khi bơm (Static Water Level - SWL, $\text{m}$).
  - $h_w$: Mực nước động đo trong giếng khi bơm ổn định (Pumping Water Level - PWL, $\text{m}$).
  - $s_{\text{aquifer}} = B_1 \cdot Q$: **Tổn thất tầng chứa nước (Aquifer Formation Loss)**. Mang bản chất dòng chảy tầng (Laminar flow) tuân theo định luật Darcy, tỷ lệ bậc nhất với lưu lượng $Q$. Hệ số $B_1$ phụ thuộc vào hệ số dẫn nước $T$ và thời gian bơm $t$.
  - $s_{\text{well}} = C_1 \cdot Q^2$: **Tổn thất vách giếng (Well Loss)**. Mang bản chất dòng chảy rối (Turbulent flow) do xoáy cuộn của dòng nước khi chuyển hướng đột ngột qua lớp sỏi lọc, chui qua các khe hẹp của ống lọc và ma sát dọc theo thành ống vách vào miệng hút của bơm. Tỷ lệ với bình phương lưu lượng $Q^2$. Hệ số $C_1$ là hệ số tổn thất giếng (Well loss coefficient).

##### 2.4.3.2 Hiệu Suất Giếng (Well Efficiency) và Năng Suất Riêng (Specific Capacity)
###### Hiệu Suất Giếng (Well Efficiency - $\eta_{\text{well}}$)
Hiệu suất giếng phản ánh mức độ hoàn hảo về mặt gia công cơ khí và mức độ phát triển súc rửa giếng:

$$\eta_{\text{well}} = \frac{s_{\text{aquifer}}}{s_w} \times 100\% = \frac{B_1 Q}{B_1 Q + C_1 Q^2} \times 100\%$$

- **Tiêu chuẩn đánh giá kỹ thuật giếng**:
  - $\eta_{\text{well}} > 70\% - 80\%$: Giếng thi công rất tốt, sỏi lọc và ống lọc thông thoáng, phát triển giếng hoàn hảo.
  - $\eta_{\text{well}} = 50\% - 70\%$: Giếng trung bình, tổn thất vách giếng bắt đầu đáng kể.
  - $\eta_{\text{well}} < 50\%$: Giếng kém chất lượng, ống lọc bị nghẹt bùn bentonite khoan hoặc bị đóng cặn hóa học nặng, cần súc rửa phục hồi giếng khẩn cấp.

###### Năng Suất Riêng của Giếng (Well Specific Capacity - $\text{SC}$)
Năng suất riêng là chỉ số thực địa quan trọng nhất biểu thị năng lực sinh nước của giếng trên mỗi mét hạ thấp mực nước:

$$\text{Năng suất riêng: } \text{SC} = \frac{Q}{s_w}$$

- **Mã phương trình**: `eq_ch02_004`
- **Đơn vị thường dùng**: $\text{m}^3/(\text{h}\cdot\text{m})$, $\text{L}/(\text{s}\cdot\text{m})$ hoặc $\text{gpm/ft}$.
- Chỉ số $\text{SC}$ được theo dõi định kỳ hàng tháng trong suốt tuổi thọ giếng. Nếu $\text{SC}$ suy giảm dần theo thời gian dù mực nước tĩnh không đổi, đó là dấu hiệu chỉ điểm chắc chắn của hiện tượng tắc nghẹt khe lọc hoặc suy thoái tầng chứa nước.

##### 2.4.3.3 Quy Trình Thử Nghiệm Bơm Giật Cấp (Step-Drawdown Test Procedure proc_ch02_03)
Để xác định các hệ số $B_1$ và $C_1$:
1. Bơm giếng liên tục qua $4$ hoặc $5$ cấp lưu lượng tăng dần liên tiếp (ví dụ: $25\% \to 50\% \to 75\% \to 100\% \to 120\%$ công suất thiết kế), mỗi cấp bơm ổn định trong $2 - 3\text{ giờ}$.
2. Ghi nhận lưu lượng $Q_i$ và độ hạ mực nước ổn định tương ứng $s_{w,i}$.
3. Biến đổi phương trình Jacob về dạng đường thẳng: $s_w / Q = B_1 + C_1 \cdot Q$.
4. Vẽ đồ thị tương quan giữa $s_w / Q$ (trục tung) và $Q$ (trục hoành). Dùng phương pháp hồi quy tuyến tính: Hệ số góc của đường thẳng chính là $C_1$, và điểm cắt trục tung chính là $B_1$.

##### 2.4.3.4 Bài Tập Tính Toán Điển Hình Hiệu Suất Giếng (Worked Example EX-CH02-03)
###### Đề bài (Problem Statement)
Một thí nghiệm bơm hút nước giật cấp (step-drawdown test) được tiến hành trên một giếng khoan khai thác công nghiệp của nhà máy nước đã xác định được:
- Hệ số tổn thất tầng chứa nước tầng: $B_1 = 0.0018\text{ ngày/m}^2$ ($155.52\text{ s/m}^2$).
- Hệ số tổn thất vách giếng chảy rối: $C_1 = 0.0000012\text{ ngày}^2/\text{m}^5$ ($8.958 \times 10^3\text{ s}^2/\text{m}^5$).
Mực nước tĩnh đo được trong giếng trước khi bơm là $H_0 = 45.0\text{ m}$ dưới mặt đất (below ground surface - bgs).
Nhà máy nước dự kiến vận hành giếng với lưu lượng thiết kế $Q = 3,000\text{ m}^3/\text{ngày}$ ($34.72\text{ L/s}$).
Hãy tính toán:
1. Độ hạ mực nước do tổn thất tầng chứa nước ($s_{\text{aquifer}}$) và do tổn thất vách giếng ($s_{\text{well}}$).
2. Tổng độ hạ mực nước thực tế trong giếng ($s_w$).
3. Cao trình mực nước động bên trong giếng khi bơm ($PWL$) tính từ mặt đất tự nhiên.
4. Hiệu suất làm việc của giếng ($\eta_{\text{well}}$).
5. Năng suất riêng của giếng ($\text{SC}$) theo các đơn vị $\text{m}^3/(\text{ngày}\cdot\text{m})$ và $\text{L}/(\text{s}\cdot\text{m})$.

###### Thông số cho trước (Given Data)
- Hệ số tầng $B_1 = 0.0018\text{ ngày/m}^2$.
- Hệ số vách $C_1 = 1.2 \times 10^{-6}\text{ ngày}^2/\text{m}^5$.
- Mực nước tĩnh $H_0 = 45.0\text{ m}$ dưới mặt đất.
- Lưu lượng thiết kế $Q = 3000.0\text{ m}^3/\text{ngày}$.

###### Lời giải Chi tiết Từng bước (Step-by-Step Solution)
- **Bước 1: Tính độ hạ mực nước do tổn thất tầng chứa nước ($s_{\text{aquifer}}$)**:
  $$s_{\text{aquifer}} = B_1 \cdot Q = 0.0018 \times 3000.0 = 5.40\text{ m}$$

- **Bước 2: Tính độ hạ mực nước do tổn thất vách giếng ($s_{\text{well}}$)**:
  $$Q^2 = (3000.0)^2 = 9,000,000\text{ m}^6/\text{ngày}^2$$
  $$s_{\text{well}} = C_1 \cdot Q^2 = 1.2 \times 10^{-6} \times 9,000,000 = 10.80\text{ m}$$

- **Bước 3: Tính tổng độ hạ mực nước thực tế trong lòng giếng ($s_w$)**:
  $$s_w = s_{\text{aquifer}} + s_{\text{well}} = 5.40 + 10.80 = 16.20\text{ m}$$

- **Bước 4: Xác định cao trình mực nước động ($PWL$)**:
  $$\text{PWL} = H_0 + s_w = 45.0 + 16.20 = 61.20\text{ m dưới mặt đất (bgs)}$$
  *(Lưu ý: Bơm chìm phải được treo ở độ sâu tối thiểu $65 - 68\text{ m}$ để đảm bảo luôn ngập sâu dưới mực nước động).*

- **Bước 5: Tính hiệu suất làm việc của giếng ($\eta_{\text{well}}$)**:
  $$\eta_{\text{well}} = \frac{s_{\text{aquifer}}}{s_w} \times 100\% = \frac{5.40}{16.20} \times 100\% = 33.33\%$$
  *Đánh giá*: Hiệu suất giếng $\eta_{\text{well}} = 33.33\% < 50\%$, tổn thất do vách giếng chiếm tới $66.67\%$ tổng độ hạ mực nước. Điều này chứng tỏ giếng bị cản trở dòng vào rất lớn (khe lọc quá nhỏ, nghẹt sỏi lọc hoặc súc rửa phát triển giếng chưa đạt), cần thực hiện sục rửa hoàn thiện lại.

- **Bước 6: Tính năng suất riêng của giếng ($\text{SC}$)**:
  $$\text{SC} = \frac{Q}{s_w} = \frac{3000.0\text{ m}^3/\text{ngày}}{16.20\text{ m}} = 185.185\text{ m}^3/(\text{ngày}\cdot\text{m})$$
  - Đổi sang đơn vị $\text{L}/(\text{s}\cdot\text{m})$:
    $$\text{SC} = \frac{185.185 \times 1000}{86,400} = 2.1433\text{ L}/(\text{s}\cdot\text{m})$$

###### Đáp số (Final Answer)
- Tổn thất tầng: $s_{\text{aquifer}} = 5.40\text{ m}$; Tổn thất giếng: $s_{\text{well}} = 10.80\text{ m}$.
- Tổng độ hạ mực nước: $s_w = 16.20\text{ m}$.
- Mực nước động: $\text{PWL} = 61.20\text{ m}$ dưới mặt đất.
- Hiệu suất giếng: $\eta_{\text{well}} = 33.33\%$ (kém, cần xử lý súc rửa).
- Năng suất riêng: $\text{SC} = 185.19\text{ m}^3/(\text{ngày}\cdot\text{m})$ ($2.14\text{ L}/(\text{s}\cdot\text{m})$).

---

#### 2.4.4 Định Cỡ Thủy Lực Ống Lọc Giếng Khoan và Chống Cát Đùn (Well Screen Sizing & Sand Pumping Prevention)
##### 2.4.4.1 Tiêu Chuẩn Vận Tốc Cửa Vào Ống Lọc (Screen Entrance Velocity Criteria)
- Thông số: **Deep Well Continuous-Slot Screen Maximum Allowable Entrance Velocity** (`dp_ch02_006`):
  $$v_{\text{screen\_entrance}} \le 0.03\text{ m/s} \quad (\approx 0.1\text{ ft/s} = 30\text{ mm/s})$$
- **Cơ sở vật lý và hóa học (Driscoll & Johnson Criteria)**:
  1. *Ngăn ngừa hiện tượng đùn cát (Sand Pumping)*: Vận tốc nước chui qua khe nhỏ hơn $0.03\text{ m/s}$ duy trì chế độ chảy tầng tuyệt đối qua lớp sỏi lọc. Lực kéo thủy động (drag force) không đủ thắng lực liên kết trọng lực của hạt cát, ngăn ngừa hoàn toàn hiện tượng cát hạt mịn bị cuốn trôi vào trong giếng làm mòn vẹt cánh bơm.
  2. *Triệt tiêu tổn thất cột áp thủy lực*: Ở vận tốc $\le 0.03\text{ m/s}$, tổn thất cột nước qua khe lọc gần như bằng không ($\Delta h < 0.01\text{ m}$).
  3. *Ngăn chặn đóng cặn hóa học (Incrustation Prevention)*: Nếu vận tốc qua khe lớn ($v > 0.05 - 0.1\text{ m/s}$), sụt áp cục bộ đột ngột làm giải phóng khí $\text{CO}_2$ tự do hòa tan trong nước ngầm, làm tăng $\text{pH}$ cục bộ tại bề mặt khe lọc và kích hoạt quá trình kết tủa Canxi cacbonat ($\text{CaCO}_3$) và hydroxit sắt ($\text{Fe}(\text{OH})_3$), làm xi măng hóa lớp sỏi lọc và bít kín khe hở ống lọc.

##### 2.4.4.2 Phương Trình Diện Tích Mở và Chiều Dài Ống Lọc (Screen Entrance Velocity Equation)
Vận tốc thực tế đi qua khe ống lọc được tính bằng công thức:

$$\text{Vận tốc vào khe: } v_{\text{entrance}} = \frac{Q}{A_{\text{open}}} = \frac{Q}{\pi \cdot d_{\text{screen}} \cdot L_{\text{screen}} \cdot C_{\text{open}} \cdot C_{\text{clog}}} \le v_{\text{allowable}}$$

- **Mã phương trình**: `eq_ch02_006`
- **Ý nghĩa các biến số**:
  - $v_{\text{entrance}}$: Vận tốc thực tế của dòng nước chui qua khe lưới ($\text{m/s}$).
  - $Q$: Lưu lượng thiết kế của giếng khoan ($\text{m}^3/\text{s}$).
  - $d_{\text{screen}}$: Đường kính ngoài danh nghĩa của ống lọc Johnson ($\text{m}$).
  - $L_{\text{screen}}$: Chiều dài hoạt động hữu hiệu của đoạn ống lọc ($\text{m}$).
  - $C_{\text{open}}$: Tỷ lệ diện tích mở danh định của ống lọc do nhà sản xuất cung cấp (dưới dạng số thập phân, ví dụ $22\% \to 0.22$).
  - $C_{\text{clog}}$: **Hệ số an toàn tắc nghẽn khe lọc** theo khuyến cáo của hiệp hội cấp nước Hoa Kỳ (AWWA Standard): thông thường lấy $C_{\text{clog}} = 0.50$ (tương ứng giả định $50\%$ diện tích mở của khe bị các hạt sỏi và cát bám bịt kín).

Từ phương trình trên, chiều dài tối thiểu cần thiết của ống lọc giếng khoan được xác định:

$$L_{\text{screen, min}} = \frac{Q}{\pi \cdot d_{\text{screen}} \cdot C_{\text{open}} \cdot C_{\text{clog}} \cdot v_{\text{allowable}}}$$

##### 2.4.4.3 Quy Trình Thiết Kế Toàn Diện Giếng Khoan Tầng Có Áp (Procedure proc_ch02_02)
1. **Bước 1: Điều tra địa chất thủy văn**:
   Khoan lỗ khoan thăm dò, kéo địa vật lý lỗ khoan (geophysical resistivity/gamma logging) để xác định chính xác cao trình nóc và đáy tầng chứa nước ($B$). Lấy mẫu đất cát tiến hành thí nghiệm rây hạt xác định $D_{10}, D_{40}, D_{60}$.
2. **Bước 2: Định cỡ ống vách và trám vữa xi măng bảo vệ**:
   Xác định chiều sâu ống chống bề mặt tối thiểu $10 - 15\text{ m}$, bơm trám vữa xi măng áp lực cao. Định cỡ đường kính ống vách khai thác đảm bảo khoảng hở hướng kính với bơm chìm $\ge 50\text{ mm}$.
3. **Bước 3: Định cỡ khe và chiều dài ống lọc Johnson**:
   Căn cứ cấp phối hạt chọn cỡ khe slot. Áp dụng công thức `eq_ch02_006` với $v_{\text{allowable}} \le 0.03\text{ m/s}$ và hệ số nghẹt $50\%$ để tính chiều dài ống lọc $L_{\text{screen}}$. Nếu chiều dài yêu cầu lớn hơn bề dày tầng chứa nước ($L > B$), phải tăng đường kính ống lọc $d_{\text{screen}}$.
4. **Bước 4: Thiết kế sỏi lọc và ống lắng cát**:
   Xác định kích thước sỏi lọc silica nhân tạo ($d_{50} = (4-6) \cdot D_{50}$), chiều dày lớp sỏi chèn $t = 100\text{ mm}$. Bố trí ống lắng cát dài $3 - 6\text{ m}$ dưới đáy ống lọc và hàn nắp đáy.

##### 2.4.4.4 Bài Tập Tính Toán Điển Hình Định Cỡ Ống Lọc Johnson (Worked Example EX-CH02-04)
###### Đề bài (Problem Statement)
Thiết kế ống lọc khe quấn liên tục bằng thép không gỉ (Johnson continuous-slot screen) cho một giếng khoan khai thác nước ngầm công nghiệp có lưu lượng bơm $Q = 3,600\text{ m}^3/\text{ngày}$ ($0.04167\text{ m}^3/\text{s} = 41.67\text{ L/s}$).
Đường kính ngoài của ống lọc được lựa chọn theo tiêu chuẩn thương phẩm là $d_{\text{screen}} = 300\text{ mm}$ ($0.30\text{ m}$).
Quy cách chế tạo ống lọc từ nhà sản xuất với cỡ khe $1.0\text{ mm}$ (khe số 40 - 40-slot) cho tỷ lệ diện tích mở là $C_{\text{open}} = 22\%$ ($0.22$).
Để đảm bảo an toàn lâu dài do sự chèn ép của các hạt sỏi lọc xung quanh và bùn cát mịn bám dính sau nhiều năm vận hành, áp dụng hệ số an toàn tắc nghẽn AWWA $C_{\text{clog}} = 0.50$ ($50\%$ diện tích khe hở khả dụng). Vận tốc dòng vào khe tối đa cho phép là $v_{\text{allowable}} \le 0.03\text{ m/s}$ ($0.1\text{ ft/s}$).
Hãy tính toán:
1. Diện tích mở thực tế yêu cầu ($A_{\text{open, req}}$).
2. Chiều dài hoạt động tối thiểu ($L_{\text{screen}}$) của đoạn ống lọc và lựa chọn chiều dài mô-đun thương phẩm tiêu chuẩn.
3. Kiểm tra vận tốc dòng vào khe ở trạng thái hoàn toàn sạch và trạng thái bị tắc nghẽn $50\%$.

###### Thông số cho trước (Given Data)
- Lưu lượng bơm $Q = 0.04167\text{ m}^3/\text{s}$.
- Đường kính ngoài ống lọc $d_{\text{screen}} = 0.30\text{ m}$.
- Tỷ lệ diện tích mở $C_{\text{open}} = 0.22$.
- Hệ số tắc nghẽn an toàn $C_{\text{clog}} = 0.50$.
- Vận tốc vào khe cho phép $v_{\text{allowable}} = 0.03\text{ m/s}$.

###### Lời giải Chi tiết Từng bước (Step-by-Step Solution)
- **Bước 1: Tính diện tích mở thực tế yêu cầu**:
  $$A_{\text{open, req}} = \frac{Q}{v_{\text{allowable}}} = \frac{0.04167\text{ m}^3/\text{s}}{0.03\text{ m/s}} = 1.389\text{ m}^2$$

- **Bước 2: Xác định chiều dài ống lọc tối thiểu**:
  - Diện tích mở hiệu dụng liên hệ với kích thước hình học ống lọc:
    $$A_{\text{open, effective}} = (\pi \cdot d_{\text{screen}} \cdot L_{\text{screen}}) \cdot C_{\text{open}} \cdot C_{\text{clog}}$$
  - Rút ra chiều dài ống lọc $L_{\text{screen}}$:
    $$L_{\text{screen}} = \frac{A_{\text{open, req}}}{\pi \cdot d_{\text{screen}} \cdot C_{\text{open}} \cdot C_{\text{clog}}}$$
  - Mẫu số:
    $$\text{Mẫu số} = \pi \times 0.30 \times 0.22 \times 0.50 = 0.103673\text{ m}$$
  - Tính chiều dài:
    $$L_{\text{screen}} = \frac{1.389}{0.103673} = 13.398\text{ m}$$
  - Chọn chiều dài mô-đun ống lọc thương phẩm tiêu chuẩn (các ống tiêu chuẩn dài $3.0\text{ m}$ hoặc $2.0\text{ m}$ ghép nối bằng mối hàn ren): **$L_{\text{design}} = 14.0\text{ m}$**.

- **Bước 3: Kiểm tra vận tốc dòng vào khe thực tế**:
  - Tổng diện tích bề mặt hình trụ của đoạn ống lọc $14.0\text{ m}$:
    $$A_{\text{cyl}} = \pi \cdot d_{\text{screen}} \cdot L_{\text{design}} = \pi \times 0.30 \times 14.0 = 13.1947\text{ m}^2$$
  - *Ở trạng thái hoàn toàn sạch (Clean screen, $100\%$ diện tích mở)*:
    $$A_{\text{open, clean}} = 13.1947 \times 0.22 = 2.9028\text{ m}^2$$
    $$v_{\text{clean}} = \frac{Q}{A_{\text{open, clean}}} = \frac{0.04167}{2.9028} = 0.01435\text{ m/s} \quad (\le 0.03\text{ m/s} \implies \text{ĐẠT})$$
  - *Ở trạng thái tắc nghẽn 50% (50% Clogged screen)*:
    $$A_{\text{open, clogged}} = 2.9028 \times 0.50 = 1.4514\text{ m}^2$$
    $$v_{\text{clogged}} = \frac{Q}{A_{\text{open, clogged}}} = \frac{0.04167}{1.4514} = 0.02871\text{ m/s} \quad (\le 0.03\text{ m/s} \implies \text{ĐẠT})$$

###### Đáp số (Final Answer)
- Diện tích mở yêu cầu: $A_{\text{open}} = 1.389\text{ m}^2$.
- Chiều dài ống lọc tính toán: $L_{\text{screen}} = 13.40\text{ m}$ (chọn ống tiêu chuẩn $14.0\text{ m}$).
- Vận tốc vào khe trạng thái sạch: $v_{\text{clean}} = 0.0144\text{ m/s}$.
- Vận tốc vào khe khi nghẹt $50\%$: $v_{\text{clogged}} = 0.0287\text{ m/s} \le 0.03\text{ m/s}$ (đáp ứng trọn vẹn tiêu chuẩn chống đùn cát và chống đóng cặn).

---

#### 2.4.5 Công Nghệ Khoan Giếng và Phát Triển Giếng (Drilling Technology, Rig Mechanics & Well Development)
##### 2.4.5.1 Các Phương Pháp Khoan Giếng Hiện Đại (Well Drilling Methodologies - Figure fig_ch02_011)
Việc thi công giếng khoan sâu sử dụng các dàn khoan tự hành gắn trên xe tải (Truck-mounted drilling rigs):
1. **Khoan xoay tuần hoàn thuận (Direct Rotary Drilling)**:
   - Dung dịch bùn khoan bentonite được bơm áp lực cao từ bể bùn qua ruột cần khoan xuống làm mát mũi khoan xoay (roller cone tricone bit hoặc PDC bit).
   - Bùn mang theo mùn khoan đất đá đi ngược lên bề mặt qua khoảng không hình xuyến giữa cần khoan và thành lỗ khoan.
   - *Chức năng của dung dịch bùn bentonite*:
     - Tạo áp lực thủy tĩnh cân bằng áp lực nước dưới đất và áp lực đất bên ngoài, chống sập vách lỗ khoan mà không cần hạ ống chống tạm.
     - Tạo một lớp màng bùn mỏng mịn cách nước (filter cake / mud cake) trát chặt lên thành lỗ khoan ngăn thất thoát nước.
     - Đưa phoi mùn khoan nổi lên mặt đất và làm mát, bôi trơn mũi khoan.
2. **Khoan xoay tuần hoàn nghịch (Reverse Circulation Rotary Drilling)**:
   - Dung dịch khoan tự chảy từ mặt đất vào lỗ khoan qua khoảng không hình xuyến, sau đó toàn bộ mùn khoan và nước được hút ngược lên qua ruột cần khoan bằng bơm hút chân không hoặc khí nén (air-lift).
   - Vận tốc dòng ngược trong cần khoan rất cao ($2 - 3\text{ m/s}$), mang được các tảng cuội sỏi lớn lên mặt đất. Áp dụng cho các giếng khoan công nghiệp đường kính cực lớn ($D = 0.5 - 1.2\text{ m}$).
3. **Khoan đập cáp (Cable-Tool Percussion Drilling)**:
   - Sử dụng choòng khoan nặng nâng lên hạ xuống liên tục bằng dây cáp để nghiền nát đất đá ở đáy giếng, sau đó dùng ống múc đáy (bailer) múc bùn phoi vụn lên. Phương pháp này khoan chậm nhưng không dùng bùn bentonite nên không làm bẩn tầng chứa nước, rất thích hợp cho địa tầng đá nứt nẻ hoặc đá vôi karst.

##### 2.4.5.2 Địa Vật Lý Lỗ Khoan (Borehole Geophysical Logging)
Trước khi thả ống vách và ống lọc, bắt buộc phải kéo cần đo địa vật lý lỗ khoan để kiểm tra chính xác ranh giới địa tầng:
- **Đo điện trở suất biểu kiến (Resistivity Log)**: Phân biệt tầng cát chứa nước ngọt (điện trở suất cao $20 - 100\ \Omega\cdot\text{m}$) với tầng sét (điện trở suất rất thấp $1 - 5\ \Omega\cdot\text{m}$) và tầng nước lợ/mặn (điện trở suất cực thấp do ion $\text{Cl}^-$ dẫn điện mạnh).
- **Đo điện thế tự nhiên (Spontaneous Potential - SP Log)**: Xác định tính thấm và ranh giới rõ nét giữa cát và sét.

##### 2.4.5.3 Phương Pháp Rửa và Phát Triển Giếng (Well Development Techniques)
Sau khi thả ống vách, ống lọc và chèn sỏi, giếng chưa thể sử dụng ngay mà phải trải qua quá trình phát triển giếng (Well Development) để đạt công suất thiết kế:
- **Mục tiêu**:
  1. Đánh tan và tẩy sạch hoàn toàn lớp màng bùn bentonite (mud cake) bám trên thành lỗ khoan.
  2. Hút sạch các hạt sét và cát mịn nằm cận kề ống lọc ra ngoài giếng.
  3. Sắp xếp lại cấu trúc các hạt sỏi lọc xung quanh ống lọc thành một tầng lọc tự nhiên có cấp phối hạt chuyển tiếp hoàn hảo (graded natural pack), tối đa hóa tính thấm của vùng cận giếng.
- **Phương pháp thực hiện**:
  - *Sục sạo bằng pít-tông kéo giật (Surge Plunger / Surge Block Swabbing)*: Pít-tông gắn gioăng cao su được kéo giật lên xuống nhanh trong lòng ống lọc, tạo chênh áp xung lực đẩy nước qua lại khe lọc đánh tan màng sét.
  - *Thổi rửa bằng khí nén (Compressed Air Jetting / Air-lifting)*: Đưa vòi phun khí áp lực cao ($p = 7 - 10\text{ bar}$) xoay tròn sát vách khe lọc để xịt bay cặn sét, đồng thời bơm nâng khí hút toàn bộ bùn cát thải ra ngoài miệng giếng.
  - Quá trình phát triển giếng kết thúc khi nước giếng bơm ra trong vắt, hàm lượng cát lơ lửng đo qua nón lắng Imhoff đạt tiêu chuẩn $< 1\text{ mg/L}$ (hoặc $< 5\text{ mg/L}$ trong 10 phút đầu bơm).

---

### 2.5 Thiết Bị Cơ Điện Khai Thác và Thủy Lực Nâng Nước (Pumping Machinery & Suction Hydraulics)
#### 2.5.1 Bơm Chìm Đa Tầng Cánh và Bơm Tuabin Trục Đứng (Submersible & Vertical Turbine Deep Well Pumps)
##### 2.5.1.1 Cấu Tạo và Lắp Đặt Bơm Chìm Giếng Sâu (Submersible Pump Assembly - Figure fig_ch02_012)
Bơm chìm giếng sâu (Submersible deep well pump) là thiết bị khai thác nước ngầm công nghiệp phổ biến nhất:
- **Động cơ điện chìm (Submersible Motor)**: Đặt ở phần dưới cùng của cụm bơm. Là loại động cơ cảm ứng xoay chiều 3 pha kín nước hoàn toàn (cấp bảo vệ IP68), khoang trong động cơ chứa đầy nước tinh khiết hoặc dầu thực vật chuyên dụng để bôi trơn ổ trượt và tản nhiệt.
- **Cụm cánh bơm ly tâm đa tầng cánh (Multi-Stage Centrifugal Impellers)**: Gắn đồng trục phía trên động cơ, nước vào cửa hút ở đoạn giữa và đi qua chuỗi cánh quạt khép kín nối tiếp nhau (từ $5$ đến $30+$ tầng cánh) làm bằng thép không gỉ hoặc đồng. Mỗi tầng cánh tăng áp lực nước thêm $5 - 15\text{ m}$ cột áp.
- **Van một chiều tích hợp (Integrated Check Valve)**: Lắp ngay tại đầu đẩy của bơm để ngăn hiện tượng nước chảy ngược làm quay ngược cánh bơm khi tắt máy và chống sốc va đập thủy lực (water hammer).
- **Ống đẩy và Cáp điện chìm**: Bơm được treo lơ lửng trong ống vách bằng cột ống thép nối bích hoặc ren (column pipe), cáp điện chịu nước cố định vào ống đẩy bằng các đai kẹp cao su.
- **Cảm biến bảo vệ chống cạn (Dry-run Protection Probes)**: Các điện cực cảm biến mực nước gắn phía trên bơm kết nối với rơ-le điều khiển tự động ngắt điện động cơ khi mực nước động tụt sâu sát miệng hút của bơm.

##### 2.5.1.2 Bơm Tuabin Trục Đứng (Vertical Line-Shaft Turbine Pumps)
Áp dụng cho các giếng khoan công nghiệp công suất khổng lồ hoặc nơi nguồn nước ngầm có nhiệt độ cao:
- Động cơ điện đặt khô ráo trên mặt sàn miệng giếng.
- Trục truyền động cơ khí bằng thép hợp kim rất dài đặt trong ống đỡ dẫn lực xoắn xuống cụm cánh bơm nhúng chìm dưới nước đáy giếng.
- Ưu điểm: Động cơ tiêu chuẩn dễ bảo trì thay thế, không sợ cháy do rò rỉ nước; nhược điểm: Lắp đặt trục truyền động dài đòi hỏi độ thẳng tuyệt đối của giếng khoan (độ nghiêng lệch $< 1^\circ$).

---

#### 2.5.2 Thủy Lực Hút Bề Mặt và Giới Hạn Hút Khí Quyển (Atmospheric Suction Lift Limits & Cavitation Mechanics)
##### 2.5.2.1 Bản Chất Vật Lý Của Chiều Cao Hút Khí Quyển và Áp Suất Hơi
Nhiều người lầm tưởng rằng máy bơm hút nước lên bằng cách "kéo" nước. Trong cơ học chất lỏng thực tế, **máy bơm không tự kéo nước lên mà chỉ tạo ra một vùng áp suất chân không thấp tại tâm cánh bơm, và chính áp suất khí quyển bề mặt ($p_{\text{atm}}$) tác động lên mặt thoáng của nguồn nước đẩy cột nước dâng lên vào họng bơm**.
Do đó, chiều cao hút tĩnh tối đa của bất kỳ loại bơm đặt cạn nào cũng bị giới hạn tuyệt đối bởi áp suất khí quyển địa phương và áp suất hóa hơi bão hòa của nước:

$$H_{\text{barometric}} = \frac{p_{\text{atm}}}{\rho \cdot g} \approx 10.33\text{ m H}_2\text{O tại mực nước biển (101,325 Pa, 4}^\circ\text{C)}$$

Khi nhiệt độ nước tăng lên, áp suất hơi bão hòa của nước ($p_v$) tăng mạnh, làm giảm chiều cao nâng khả dụng:
- Ở $20^\circ\text{C}$: $p_v = 2,338\text{ Pa} \implies H_v = p_v / \gamma = 0.24\text{ m}$.
- Ở $30^\circ\text{C}$: $p_v = 4,246\text{ Pa} \implies H_v = p_v / \gamma = 0.44\text{ m}$.
- Ở $40^\circ\text{C}$: $p_v = 7,384\text{ Pa} \implies H_v = p_v / \gamma = 0.76\text{ m}$.

##### 2.5.2.2 Phương Trình Chiều Cao Hút Tối Đa Cho Phép và Hiện Tượng Xâm Thực (NPSH & Cavitation)
###### Phương trình Chiều cao Hút Tĩnh Tối đa (Maximum Allowable Static Suction Lift)
Chiều cao hút tĩnh tối đa cho phép lắp đặt bơm đặt cạn trên mặt đất được xác định qua phương trình cân bằng năng lượng:

$$\text{Chiều cao hút tối đa: } h_{\text{suction, max}} = \frac{p_{\text{atm}} - p_v}{\rho \cdot g} - h_{L,\text{suction}} - \text{NPSH}_{\text{req}} - \text{Safety Margin}$$

- **Mã phương trình**: `eq_ch02_009`
- **Ý nghĩa các biến số**:
  - $h_{\text{suction, max}}$: Khoảng cách thẳng đứng tối đa từ mực nước kiệt động của nguồn đến tim trục cánh bơm ($\text{m}$).
  - $p_{\text{atm}}$: Áp suất khí quyển tuyệt đối tại cao trình công trình ($\text{Pa}$, suy giảm theo độ cao địa hình: $p_{\text{atm}} = 101,325 \cdot [1 - 2.25577 \times 10^{-5} \cdot z]^{5.25588}$).
  - $p_v$: Áp suất hơi bão hòa của nước tại nhiệt độ vận hành cao nhất mùa hè ($\text{Pa}$).
  - $\rho$: Khối lượng riêng của nước ($\text{kg/m}^3$).
  - $g$: Gia tốc trọng trường ($9.81\text{ m/s}^2$).
  - $h_{L,\text{suction}}$: Tổng tổn thất ma sát đường dài và tổn thất cục bộ (van chân, cút góc) trong đường ống hút ($\text{m}$).
  - $\text{NPSH}_{\text{req}}$: Cột áp hút thực dương đòi hỏi của máy bơm do nhà sản xuất công bố (Net Positive Suction Head Required, thường từ $2.0 - 4.5\text{ m}$).
  - $\text{Safety Margin}$: Hệ số dự phòng an toàn chống xâm thực (quy chuẩn tối thiểu $0.50\text{ m}$).

###### Cơ Chế Xâm Thực Thủy Lực (Cavitation Mechanics)
Nếu lắp đặt bơm ở chiều cao vượt quá $h_{\text{suction, max}}$, áp suất tuyệt đối tại mắt cánh bơm ($p_{\text{impeller}}$) sẽ tụt xuống dưới áp suất hóa hơi bão hòa của chất lỏng ($p_{\text{impeller}} < p_v$).
- Hiện tượng: Nước sôi bốc hơi ngay ở nhiệt độ thường, tạo thành hàng triệu bọt khí hơi siêu nhỏ.
- Phá hủy: Khi các bọt khí này bị cuốn trôi sang vùng có áp suất cao ở rìa ngoài cánh quạt, chúng co lại và nổ vỡ tức thì (microscopic implosions) tạo ra các tia vi phản lực lỏng (liquid micro-jets) với vận tốc $> 1000\text{ m/s}$ và áp suất va đập cục bộ $> 10,000\text{ bar}$. Các tia phản lực này bắn phá liên tục làm rỗ tổ ong bề mặt cánh kim loại, gây tiếng nổ lách tách như bắn sỏi trong buồng bơm, rung lắc dữ dội và làm tụt hoàn toàn lưu lượng bơm.

##### 2.5.2.3 Bài Tập Tính Toán Điển Hình Chiều Cao Hút và Kiểm Tra Xâm Thực (Worked Example EX-CH02-06)
###### Đề bài (Problem Statement)
Đánh giá xem một máy bơm ly tâm đặt cạn lấy nước thô từ hố hút của trạm thu ven bờ sông lắp đặt tại một vị trí có cao trình địa hình $z = 250\text{ m}$ so với mực nước biển có thể vận hành an toàn không bị xâm thực hay không khi mực nước kiệt động trong hố hút cách tim trục máy bơm một khoảng thẳng đứng $h_{\text{lift}} = 5.20\text{ m}$.
Nhiệt độ nước sông cao nhất vào mùa hè là $T = 30^\circ\text{C}$ (ứng với áp suất hơi bão hòa $p_v = 4.246\text{ kPa}$, khối lượng riêng của nước $\rho = 995.7\text{ kg/m}^3$, trọng lượng riêng $\gamma = 9,768\text{ N/m}^3$).
Tại cao trình $z = 250\text{ m}$, áp suất khí quyển thực tế đo được là $p_{\text{atm}} = 98.37\text{ kPa}$.
Tổng tổn thất ma sát qua đường ống hút, van chân và cút cong được tính toán là $h_{L,\text{suction}} = 0.85\text{ m}$.
Đặc tính kỹ thuật của máy bơm do nhà sản xuất cung cấp yêu cầu cột áp hút thực dương $\text{NPSH}_{\text{req}} = 2.80\text{ m}$. Quy chuẩn thiết kế đòi hỏi hệ số an toàn tối thiểu là $0.50\text{ m}$.
Hãy tính toán:
1. Cột áp áp suất khí quyển $H_{\text{atm}}$ và cột áp hóa hơi $H_v$ tính bằng mét nước.
2. Chiều cao hút tĩnh tối đa cho phép ($h_{\text{suction, max}}$) của máy bơm tại công trình.
3. Cột áp hút thực dương khả dụng ($\text{NPSH}_a$) của hệ thống và kiểm tra điều kiện an toàn chống xâm thực của máy bơm.

###### Thông số cho trước (Given Data)
- Cao trình địa hình $z = 250.0\text{ m}$.
- Áp suất khí quyển $p_{\text{atm}} = 98,370.0\text{ Pa}$ ($98.37\text{ kPa}$).
- Áp suất hơi bão hòa ở $30^\circ\text{C}$: $p_v = 4,246.0\text{ Pa}$ ($4.246\text{ kPa}$).
- Trọng lượng riêng của nước $\gamma = 9,768.0\text{ N/m}^3$.
- Chiều cao hút thực tế thiết kế $h_{\text{lift}} = 5.20\text{ m}$.
- Tổn thất ống hút $h_{L,\text{suction}} = 0.85\text{ m}$.
- Cột áp đòi hỏi $\text{NPSH}_{\text{req}} = 2.80\text{ m}$.
- Hệ số an toàn $\text{Safety Margin} = 0.50\text{ m}$.

###### Lời giải Chi tiết Từng bước (Step-by-Step Solution)
- **Bước 1: Tính toán các cột áp áp suất (Pressure Heads)**:
  - Cột áp khí quyển tương đương:
    $$H_{\text{atm}} = \frac{p_{\text{atm}}}{\gamma} = \frac{98,370}{9,768} = 10.0706\text{ m}$$
  - Cột áp hơi bão hòa tương đương:
    $$H_v = \frac{p_v}{\gamma} = \frac{4,246}{9,768} = 0.4347\text{ m}$$

- **Bước 2: Tính chiều cao hút tĩnh tối đa cho phép ($h_{\text{suction, max}}$)**:
  - Áp dụng phương trình `eq_ch02_009`:
    $$h_{\text{suction, max}} = (H_{\text{atm}} - H_v) - h_{L,\text{suction}} - \text{NPSH}_{\text{req}} - \text{Safety Margin}$$
  - Cột áp hữu hiệu trước tổn thất:
    $$H_{\text{atm}} - H_v = 10.0706 - 0.4347 = 9.6359\text{ m}$$
  - Tổng các tổn thất và yêu cầu kỹ thuật:
    $$\Sigma_{\text{losses}} = h_{L,\text{suction}} + \text{NPSH}_{\text{req}} + \text{Safety Margin} = 0.85 + 2.80 + 0.50 = 4.150\text{ m}$$
  - Chiều cao hút tối đa cho phép:
    $$h_{\text{suction, max}} = 9.6359 - 4.150 = 5.4859\text{ m} \approx 5.49\text{ m}$$

- **Bước 3: So sánh với chiều cao hút thực tế**:
  - Chiều cao hút thiết kế: $h_{\text{lift}} = 5.20\text{ m}$.
  - So sánh: $h_{\text{lift}} = 5.20\text{ m} \le h_{\text{suction, max}} = 5.49\text{ m}$.
  - *Kết luận sơ bộ*: Máy bơm được lắp đặt hợp lệ trong phạm vi chiều cao cho phép.

- **Bước 4: Tính toán cột áp hút thực dương khả dụng ($\text{NPSH}_a$)**:
  $$\text{NPSH}_a = H_{\text{atm}} - H_v - h_{\text{lift}} - h_{L,\text{suction}}$$
  $$\text{NPSH}_a = 10.0706 - 0.4347 - 5.20 - 0.85 = 9.6359 - 6.050 = 3.5859\text{ m} \approx 3.59\text{ m}$$

- **Bước 5: Kiểm tra độ an toàn chống xâm thực**:
  - Chênh lệch cột áp thực dương:
    $$\Delta \text{NPSH} = \text{NPSH}_a - \text{NPSH}_{\text{req}} = 3.5859 - 2.80 = +0.7859\text{ m} \approx +0.79\text{ m}$$
  - So sánh với biên dự phòng quy chuẩn:
    $$\Delta \text{NPSH} = 0.79\text{ m} \ge 0.50\text{ m} \implies \text{ĐẠT AN TOÀN TUYỆT ĐỐI}$$
  - *Đánh giá*: Máy bơm sẽ vận hành êm ái, hoàn toàn không xảy ra hiện tượng bốc hơi xâm thực tại mép cánh bơm.

###### Đáp số (Final Answer)
- Cột áp khí quyển $H_{\text{atm}} = 10.07\text{ m}$; Cột áp hóa hơi $H_v = 0.44\text{ m}$.
- Chiều cao hút tĩnh tối đa cho phép: $h_{\text{suction, max}} = 5.49\text{ m}$.
- Cột áp khả dụng: $\text{NPSH}_a = 3.59\text{ m} > \text{NPSH}_{\text{req}} = 2.80\text{ m}$ (biên an toàn $+0.79\text{ m} \ge 0.50\text{ m}$, máy bơm đạt chuẩn an toàn xâm thực).

---

#### 2.5.3 Cơ Học và Động Lực Học Bơm Tay Pit-tông Tịnh Tiến Nông Thôn (Reciprocating Hand Well Pump Mechanics)
##### 2.5.3.1 Cấu Tạo Cơ Khí và Chu Trình Hoạt Động Hai Thì (Two-Stroke Cyclic Valve Mechanics)
Bơm tay giếng khoan nông thôn (như loại Bơm số 6 - No. 6 Pump, Bơm Rower, hoặc India Mark II/Afridev) là dạng máy thủy lực thể tích tịnh tiến đơn cấp (Single-acting positive displacement pump) (Figure `fig_ch02_012`):
- **Cấu tạo cơ khí chính**:
  1. *Thân xilanh (Cylinder bore)*: Bằng gang mài bóng hoặc bọc lót đồng/inox/PVC, đường kính $d_{\text{piston}} = 50 - 100\text{ mm}$.
  2. *Cơ cấu đòn bẩy tay gạt (Lever handle)*: Điểm tựa bản lề (fulcrum pin) chia tay đòn thành hai phần: tay đòn dài chịu lực ấn tay ($L_{\text{long}}$) và tay đòn ngắn nối cần kéo ($L_{\text{short}}$).
  3. *Cần bơm (Connecting rod)*: Bằng thép tròn truyền chuyển động từ tay gạt xuống pít-tông.
  4. *Quả pít-tông (Plunger / Piston)*: Gắn gioăng da hoặc cao su hình nón đệm kín vách xilanh. Trên thân pít-tông tích hợp một **van xả một chiều (Discharge check valve / Plunger valve)**.
  5. *Van đáy hút (Foot valve / Suction check valve)*: Đặt ở đáy xilanh, là van bản lề một chiều bằng đồng bọc da.
- **Chu trình hoạt động hai thì tuần hoàn**:
  - **Kỳ Đi Lên (Upstroke - Người vận hành ấn tay gạt xuống)**:
    - Cần bơm kéo pít-tông đi lên. Trọng lượng của cột nước phía trên nén chặt làm **van pít-tông đóng kín hoàn toàn**.
    - Pít-tông nâng toàn bộ khối nước nằm phía trên nó dâng lên và tràn ra ngoài vòi xả.
    - Đồng thời, sự di chuyển đi lên của pít-tông tạo ra một độ chân không áp suất âm bên dưới buồng xilanh. Lực chênh áp khí quyển đội **van chân (foot valve) mở bung ra**, hút nước mới từ giếng ngầm dâng lên lấp đầy khoang xilanh dưới pít-tông.
  - **Kỳ Đi Xuống (Downstroke - Người vận hành nhấc tay gạt lên)**:
    - Cần bơm đẩy pít-tông đi xuống. Áp lực nén thủy tĩnh của nước trong khoang dưới ép **van chân đóng sập lại**, giữ chặt cột nước không bị tụt trở lại giếng.
    - Dòng nước bị dồn ép đội ngược **van pít-tông mở tung ra**, cho phép toàn bộ lượng nước ở khoang dưới chuyển tiếp chảy tràn qua ruột pít-tông lên chiếm chỗ ở khoang xilanh phía trên pít-tông, chuẩn bị cho chu trình đẩy tiếp theo.

##### 2.5.3.2 Phân Loại Bơm Tay Nông vs Bơm Giếng Sâu (Shallow vs Deep Hand Pumps)
1. **Bơm hút đặt cạn xilanh bề mặt (Shallow Suction Hand Pump - Bơm No. 6)**:
   - Xilanh đặt ngay bên trên mặt đất trong thân bơm.
   - Ống hút cắm thẳng xuống nước ngầm.
   - Thông số: **Reciprocating Shallow Hand Pump Practical Suction Lift Limit** (`dp_ch02_015`):
     $$H_{\text{suction\_handpump}} = 6.0 - 7.5\text{ m} \quad (\text{giới hạn lý thuyết: } 10.33\text{ m})$$
   - Nếu mực nước ngầm tụt sâu quá $7.5\text{ m}$, bơm sẽ hoàn toàn mất khả năng hút nước do rò rỉ khí qua gioăng da và giới hạn bốc hơi chân không.
2. **Bơm tay giếng sâu xilanh đáy (Deep-Well Reciprocating Hand Pump - India Mark II / Afridev)**:
   - Thông số: **Deep Well Hand Pump Operating Depth Range** (`dp_ch02_016`):
     $$H_{\text{deep\_handpump}} = 15 - 45\text{ m} \quad (\text{đạt tới } 80\text{ m})$$
   - Xilanh bơm và cụm van không đặt trên mặt đất mà được thả chìm sâu dưới mực nước ngầm đáy giếng.
   - Cần bơm bằng thép kéo dài suốt chiều sâu giếng nối từ tay gạt xuống xilanh đáy.
   - Do pít-tông nhúng ngập trong nước, bơm hoạt động theo nguyên lý **đẩy trực tiếp cột nước lên bề mặt** chứ không dùng lực hút khí quyển, do đó triệt tiêu hoàn toàn giới hạn hút chân không $7.5\text{ m}$.

##### 2.5.3.3 Năng Suất Lưu Lượng Thể Tích Lý Thuyết và Thực Tế (Hand Pump Discharge Equations)
Thể tích nước xả ra trong một hành trình đơn chính là thể tích hình trụ quét bởi pít-tông:

$$V_{\text{stroke}} = A_{\text{piston}} \cdot L_{\text{stroke}} = \frac{\pi d_{\text{piston}}^2}{4} \cdot L_{\text{stroke}}$$

Lưu lượng thể tích lý thuyết của bơm tay tính theo phút:

$$\text{Lưu lượng lý thuyết: } Q_{\text{theoretical}} = A_{\text{piston}} \cdot L_{\text{stroke}} \cdot n = \frac{\pi d_{\text{piston}}^2}{4} \cdot L_{\text{stroke}} \cdot n$$

- **Mã phương trình**: `eq_ch02_010`
- **Ý nghĩa các biến số**:
  - $Q_{\text{theoretical}}$: Lưu lượng nước lý thuyết sinh ra ($\text{m}^3/\text{phút}$ hoặc $\text{L/phút}$).
  - $d_{\text{piston}}$: Đường kính trong của xilanh/pít-tông ($\text{m}$).
  - $L_{\text{stroke}}$: Chiều dài hành trình tịnh tiến của pít-tông ($\text{m}$). 
    - Thông số thiết kế: **Reciprocating Hand Pump Plunger Stroke Length** (`dp_ch02_017`): $L_{\text{stroke}} = 100 - 250\text{ mm}$ ($0.10 - 0.25\text{ m}$).
  - $n$: Tần số dập tay bơm của người sử dụng ($\text{nhịp/phút}$).
    - Thông số thiết kế: **Hand Pump Operating Stroke Frequency** (`dp_ch02_018`): $n = 30 - 40\text{ nhịp/phút}$ (tần suất dập thoải mái của con người).
- **Lưu lượng thực tế ($Q_{\text{actual}}$)**: Do sự chậm đóng của van lật và rò rỉ nước qua khe hở gioăng pít-tông, lưu lượng thực tế bị suy giảm bởi hệ số hiệu suất thể tích ($\eta_v = 80\% - 90\%$):
  $$Q_{\text{actual}} = \eta_v \cdot Q_{\text{theoretical}} \approx 15 - 30\text{ L/phút} \quad (1.0 - 1.8\text{ m}^3/\text{h})$$

##### 2.5.3.4 Động Lực Học Đòn Bẩy và Lực Vận Hành Công Thái Học (Hand Pump Lever Dynamics & Ergonomic Force)
###### Cân Bằng Momen Lực Quanh Điểm Tựa Bản Lề (Fulcrum Moment Equilibrium)
Xét trạng thái tới hạn ở kỳ đi lên (upstroke) khi người vận hành dùng hai tay ấn chuôi tay gạt xuống:
- **Tải trọng nâng thẳng đứng tác dụng lên cần bơm ($W_{\text{total}}$)**:
  $$W_{\text{total}} = F_{\text{water}} + W_{\text{rod}} + W_{\text{plunger}}$$
  Trong đó:
  - $F_{\text{water}} = \rho \cdot g \cdot A_{\text{piston}} \cdot H_{\text{lift}}$: Trọng lượng của toàn bộ cột nước nằm trên pít-tông được nâng lên ($\text{N}$).
  - $W_{\text{rod}} = m_{\text{rod}} \cdot g$: Trọng lượng bản thân của hệ thống cần bơm thép ($\text{N}$).
  - $W_{\text{plunger}}$: Khối lượng cụm pít-tông và van xả ($\text{N}$).
  - $H_{\text{lift}}$: Chiều cao cột nước nâng từ mực nước động giếng lên tới miệng vòi xả ($\text{m}$).
- **Cân bằng momen quanh trục quay bản lề (Lever Fulcrum)**:
  $$F_{\text{handle}} \cdot L_{\text{long}} = W_{\text{total}} \cdot L_{\text{short}}$$

###### Phương trình Lực Ấn Tay Vận Hành Bơm (Manual Handle Effort Force Equation)
Lực tác dụng cần thiết của người vận hành đặt lên chuôi tay gạt:

$$\text{Lực ấn tay gạt: } F_{\text{handle}} = \frac{L_{\text{short}}}{L_{\text{long}}} \cdot \left( W_{\text{rod}} + W_{\text{plunger}} + \rho g A_{\text{piston}} H_{\text{lift}} \right)$$

- **Mã phương trình**: `eq_ch02_011`
- **Tỷ số lợi cơ học (Mechanical Advantage)**: $\text{MA} = L_{\text{long}} / L_{\text{short}}$ thường được thiết kế trong khoảng $4:1$ đến $8:1$ (tiêu chuẩn phổ thông là $6:1$).
- **Tiêu chuẩn công thái học nhân trắc học (Ergonomics)**: Để phụ nữ, người già và trẻ em ở nông thôn có thể vận hành bơm liên tục trong $15 - 20\text{ phút}$ mà không kiệt sức, lực ấn tay tối đa $F_{\text{handle}}$ phải được khống chế $\le 50 - 80\text{ N}$ ($\approx 5 - 8\text{ kgf}$). Nếu giếng quá sâu ($H_{\text{lift}} > 30\text{ m}$), bắt buộc phải giảm đường kính pít-tông $d_{\text{piston}}$ (từ $75\text{ mm}$ xuống $50\text{ mm}$) hoặc tăng cánh tay đòn dài để giảm lực ấn tay.

##### 2.5.3.5 Quy Trình Lựa Chọn và Lắp Đặt Bơm Tay (Procedure proc_ch02_04)
1. **Bước 1: Đánh giá độ sâu mực nước ngầm**:
   Đo mực nước động mùa kiệt thấp nhất. Nếu $\le 7.0\text{ m}$, chọn bơm hút nông No. 6. Nếu $> 7.0\text{ m}$, bắt buộc chọn bơm giếng sâu India Mark II/Afridev có xilanh thả đáy.
2. **Bước 2: Tính toán lưu lượng và định cỡ kích thước xilanh**:
   Tính $Q = \eta_v \cdot A_{\text{piston}} \cdot L_{\text{stroke}} \cdot n$. Với $n = 35\text{ nhịp/phút}$, lựa chọn đường kính xilanh phù hợp với nhu cầu cấp nước cộng đồng.
3. **Bước 3: Thiết kế đòn bẩy cơ học và kiểm tra lực công thái học**:
   Xác định chiều dài tay đòn dài $L_{\text{long}}$ và tay đòn ngắn $L_{\text{short}}$. Áp dụng công thức `eq_ch02_011` để tính $F_{\text{handle}}$. Đảm bảo $F_{\text{handle}} \le 60 - 80\text{ N}$.
4. **Bước 4: Thi công sân giếng bê tông và niêm phong vệ sinh**:
   Đổ sân bê tông cốt thép bán kính $R \ge 1.5\text{ m}$, mương thoát nước dài $\ge 5\text{ m}$, lắp gioăng nắp đậy kín miệng giếng chống côn trùng xâm nhập.

##### 2.5.3.6 Bài Tập Tính Toán Điển Hình Bơm Tay Pit-tông Tịnh Tiến (Worked Example EX-CH02-07)
###### Đề bài (Problem Statement)
Một trạm cấp nước sạch nông thôn lắp đặt một máy bơm tay pit-tông tịnh tiến (loại Bơm số 6 - No. 6 type).
Xilanh bơm có đường kính trong $d_{\text{piston}} = 75\text{ mm}$ ($0.075\text{ m}$) và chiều dài hành trình làm việc của pít-tông là $L_{\text{stroke}} = 180\text{ mm}$ ($0.180\text{ m}$). Người vận hành dập bơm với tần số trung bình $n = 35\text{ nhịp/phút}$. Hệ số hiệu suất thể tích của bơm do hao hụt van xả là $\eta_v = 88\%$ ($0.88$).
Mực nước kiệt trong giếng cách vòi xả một khoảng thẳng đứng $H_{\text{lift}} = 6.0\text{ m}$.
Cơ cấu tay gạt đòn bẩy có chiều dài tay đòn chịu lực (effort arm) từ khớp bản lề đến tay cầm là $L_{\text{long}} = 900\text{ mm}$ ($0.90\text{ m}$), và chiều dài tay đòn tải (load arm) từ khớp bản lề đến khớp nối cần bơm là $L_{\text{short}} = 150\text{ mm}$ ($0.15\text{ m}$), tạo tỷ số lợi cơ học $6:1$.
Tổng khối lượng của cần bơm và cụm pít-tông kim loại là $m_{\text{rod}} = 3.5\text{ kg}$. Khối lượng riêng của nước là $\rho = 1,000\text{ kg/m}^3$ và gia tốc trọng trường $g = 9.81\text{ m/s}^2$.
Hãy tính toán:
1. Thể tích nước dịch chuyển trong một hành trình ($V_{\text{stroke}}$) tính bằng lít.
2. Lưu lượng nước xả lý thuyết ($Q_{\text{theoretical}}$) và lưu lượng nước xả thực tế ($Q_{\text{actual}}$) của bơm tay theo các đơn vị $\text{L/phút}$ và $\text{m}^3/\text{h}$.
3. Tải trọng thủy tĩnh do cột nước nâng tác dụng lên mặt pít-tông ($F_{\text{water}}$) trong kỳ đi lên (upstroke).
4. Tổng tải trọng kéo thẳng đứng tác dụng lên cần bơm ($W_{\text{total}}$).
5. Lực ấn tay thủ công ($F_{\text{handle}}$) người vận hành cần tác dụng lên tay gạt và đánh giá tính phù hợp công thái học.

###### Thông số cho trước (Given Data)
- Đường kính pít-tông $d_{\text{piston}} = 0.075\text{ m}$.
- Hành trình pít-tông $L_{\text{stroke}} = 0.180\text{ m}$.
- Tần số dập $n = 35.0\text{ nhịp/phút}$.
- Hiệu suất thể tích $\eta_v = 0.88$.
- Chiều cao nâng nước $H_{\text{lift}} = 6.0\text{ m}$.
- Tay đòn dài $L_{\text{long}} = 0.90\text{ m}$.
- Tay đòn ngắn $L_{\text{short}} = 0.15\text{ m}$.
- Khối lượng cần và pít-tông $m_{\text{rod}} = 3.5\text{ kg}$.
- Khối lượng riêng $\rho = 1000.0\text{ kg/m}^3$.

###### Lời giải Chi tiết Từng bước (Step-by-Step Solution)
- **Bước 1: Tính diện tích pít-tông và thể tích một hành trình**:
  - Diện tích mặt cắt ngang của pít-tông:
    $$A_{\text{piston}} = \frac{\pi \cdot d_{\text{piston}}^2}{4} = \frac{\pi \times (0.075)^2}{4} = \frac{\pi \times 0.005625}{4} = 0.00441786\text{ m}^2$$
  - Thể tích nước dịch chuyển trong một hành trình quét:
    $$V_{\text{stroke}} = A_{\text{piston}} \cdot L_{\text{stroke}} = 0.00441786 \times 0.180 = 0.00079521\text{ m}^3 = 0.7952\text{ L/hành trình}$$

- **Bước 2: Tính lưu lượng nước bơm xả**:
  - Lưu lượng lý thuyết (`eq_ch02_010`):
    $$Q_{\text{theoretical}} = V_{\text{stroke}} \times n = 0.79521 \times 35 = 27.832\text{ L/phút}$$
  - Lưu lượng thực tế có xét đến hiệu suất thể tích $\eta_v = 0.88$:
    $$Q_{\text{actual}} = Q_{\text{theoretical}} \times \eta_v = 27.832 \times 0.88 = 24.492\text{ L/phút}$$
  - Quy đổi sang $\text{m}^3/\text{h}$:
    $$Q_{\text{actual}} = \frac{24.492 \times 60}{1000} = 1.4695\text{ m}^3/\text{h} \approx 1.47\text{ m}^3/\text{h}$$

- **Bước 3: Tính tải trọng thủy tĩnh của cột nước trên pít-tông ($F_{\text{water}}$)**:
  - Khối lượng cột nước nằm trên pít-tông:
    $$m_{\text{water}} = \rho \cdot A_{\text{piston}} \cdot H_{\text{lift}} = 1000 \times 0.00441786 \times 6.0 = 26.507\text{ kg}$$
  - Trọng lực của cột nước:
    $$F_{\text{water}} = m_{\text{water}} \cdot g = 26.507 \times 9.81 = 260.035\text{ N}$$

- **Bước 4: Tính tổng tải trọng thẳng đứng trên cần bơm ($W_{\text{total}}$)**:
  - Trọng lượng cơ khí của cần và pít-tông:
    $$W_{\text{rod}} = m_{\text{rod}} \cdot g = 3.5 \times 9.81 = 34.335\text{ N}$$
  - Tổng lực kéo thẳng đứng ở đầu cần bơm:
    $$W_{\text{total}} = F_{\text{water}} + W_{\text{rod}} = 260.035 + 34.335 = 294.37\text{ N} \quad (\approx 30.0\text{ kgf})$$

- **Bước 5: Tính lực ấn tay thủ công lên chuôi tay gạt ($F_{\text{handle}}$)**:
  - Áp dụng phương trình đòn bẩy cơ học (`eq_ch02_011`):
    $$F_{\text{handle}} = W_{\text{total}} \cdot \left(\frac{L_{\text{short}}}{L_{\text{long}}}\right)$$
  - Tỷ số cánh tay đòn:
    $$\frac{L_{\text{short}}}{L_{\text{long}}} = \frac{0.15}{0.90} = \frac{1}{6} = 0.166667$$
  - Tính lực ấn:
    $$F_{\text{handle}} = 294.37 \times \frac{1}{6} = 49.0617\text{ N} \approx 49.06\text{ N}$$
  - Quy đổi tương đương theo kilôgam lực:
    $$F_{\text{handle, kgf}} = \frac{49.0617}{9.81} \approx 5.0\text{ kgf}$$
  - *Đánh giá công thái học*: Lực ấn $F_{\text{handle}} = 49.06\text{ N} \approx 5.0\text{ kgf} \le 60\text{ N}$, lực rất nhẹ và êm ái, phụ nữ và học sinh đều có thể thao tác bơm nước dễ dàng trong thời gian dài.

###### Đáp số (Final Answer)
- Thể tích một hành trình: $V_{\text{stroke}} = 0.795\text{ L/hành trình}$.
- Lưu lượng thực tế: $Q_{\text{actual}} = 24.49\text{ L/phút}$ ($1.47\text{ m}^3/\text{h}$).
- Tải trọng cột nước trên pít-tông: $F_{\text{water}} = 260.04\text{ N}$.
- Tổng lực kéo cần bơm: $W_{\text{total}} = 294.37\text{ N}$.
- Lực ấn tay gạt vận hành: $F_{\text{handle}} = 49.06\text{ N}$ ($5.0\text{ kgf}$, đạt chuẩn công thái học xuất sắc).

---

### 2.6 Chẩn Đoán Sự Cố Vận Hành và Biện Pháp Khắc Phục (Troubleshooting & Failure Modes)
Bảng tổng hợp chẩn đoán sự cố chuyên sâu cho toàn bộ hệ thống thu nước mặt và nước ngầm:

#### 2.6.1 Sự Cố Hệ Thống Thu Nước Mặt (Surface Intake Operational Diagnostics)
##### 2.6.1.1 Sự Cố Tắc Nghẽn Song Chắn Rác và Lưới Chắn Tinh (Intake Screen Clogging)
- **Mã sự cố**: `tb_ch02_01`
- **Triệu chứng nhận biết (Symptoms)**:
  - Mực nước trong ngăn hút (wet well) của trạm bơm tụt thấp đột ngột dù mực nước sông hồ bên ngoài vẫn cao.
  - Chênh lệch mực nước đo qua cảm biến siêu âm phía trước và phía sau song chắn rác tăng vọt ($\Delta h > 0.20 - 0.50\text{ m}$).
  - Máy bơm nước thô phát ra tiếng ồn rít xâm thực dữ dội, áp suất đồng hồ đầu đẩy dao động mạnh, động cơ bị quá tải nhiệt do chạy thiếu nước.
- **Nguyên nhân gốc rễ (Root Causes)**:
  - Lượng rác nổi khổng lồ, cành cây, bèo tây (lục bình), túi nilon và thảm cỏ mục trôi dạt dồn dập sau các đợt mưa bão đầu mùa.
  - Sinh vật bám (biofouling): Hà hến, trai sông, rêu tảo phát triển bám thành lớp dày bịt kín các khe hở của tấm lưới.
- **Biện pháp kỹ thuật khắc phục (Remedial Engineering Actions)**:
  1. *Khẩn cấp*: Chuyển chế độ vận hành máy cào rác tự động (Trash rakes) và băng chuyền lưới chắn tinh từ chế độ hẹn giờ sang chế độ chạy liên tục $100\%$ công suất; tăng áp lực dàn vòi phun rửa ngược (backwash sprays) lên $4 - 6\text{ bar}$.
  2. *Bảo dưỡng*: Cử thợ lặn chuyên nghiệp mang thiết bị thủy lực xuống cào phá mảng bám hà hến tại mặt ngoài cửa thu chìm; châm Clo khử trùng định kỳ (Shock chlorination) tại miệng thu để tiêu diệt mầm ấu trùng hà hến bám dính.

##### 2.6.1.2 Sự Cố Băng Kim (Frazil Ice) và Bồi Lấp Phù Sa Cửa Thu (Frazil Ice & Siltation)
- **Mã sự cố**: `tb_ch02_02`
- **Triệu chứng nhận biết (Symptoms)**:
  - Giảm lưu lượng đột ngột vào mùa đông băng giá hoặc sau đợt lũ bùn phù sa lớn.
  - Áp lực kế tại miệng thu tụt giảm sâu; máy bơm hút lẫn nhiều cát hạt thô làm đục nước thô đưa lên WTP.
- **Nguyên nhân gốc rễ (Root Causes)**:
  - Hiện tượng băng kim (Frazil Ice): Nước sông ở nhiệt độ siêu lạnh ($0^\circ\text{C}$ đến $-0.1^\circ\text{C}$) chuyển động hỗn loạn kết tinh thành các tinh thể băng dạng kim hình đĩa nhỏ. Khi chạm vào các thanh song sắt lạnh, băng kim bám dính tức thì và phát triển nhanh chóng bịt kín toàn bộ khe hở chỉ trong vài chục phút.
  - Hiện tượng bồi lấp (Siltation): Dòng lũ mang lượng bùn cát di đáy khổng lồ bồi lấp chôn vùi toàn bộ miệng loa thu chìm dưới lớp cát dày $1 - 2\text{ m}$.
- **Biện pháp kỹ thuật khắc phục (Remedial Engineering Actions)**:
  1. *Chống băng kim*: Bố trí hệ thống sấy nóng điện trở điện áp thấp trực tiếp trong các nan sắt song chắn rác; lắp đặt hệ thống sục khí nén đáy (compressed air bubbling system) để đẩy dòng nước ấm hơn từ tầng đáy nổi lên làm tan tinh thể băng kim.
  2. *Xử lý bồi lấp*: Luôn thiết kế cao trình ngưỡng cửa thu cao hơn đáy sông tối thiểu $0.5 - 1.0\text{ m}$; bố trí van xả rửa ngược bằng nước áp lực cao (backflushing pipeline) từ nhà máy xả ngược ra đầu thu để thổi bay khối cát bồi lấp; định kỳ nạo vét luồng hút bằng tàu hút bùn chuyên dụng.

---

#### 2.6.2 Sự Cố Hệ Thống Giếng Nước Ngầm (Groundwater Well Diagnostics)
##### 2.6.2.1 Hiện Tượng Giếng Khoan Bị Đùn Cát và Mài Mòn Cánh Bơm (Well Sand Pumping & Screen Abrasion)
- **Mã sự cố**: `tb_ch02_03`
- **Triệu chứng nhận biết (Symptoms)**:
  - Nước bơm lên đục, xả mẫu qua bình kiểm tra cát thấy tích tụ nhiều cặn cát hạt nhọn ($> 5\text{ mg/L}$).
  - Cánh quạt máy bơm chìm bị mài mòn vẹt nhanh chóng chỉ sau vài tháng, lưu lượng và cột áp bơm tụt giảm nghiêm trọng.
  - Cát lắng tích tụ dày trong bể tiếp xúc và hố lắng cát của nhà máy xử lý.
- **Nguyên nhân gốc rễ (Root Causes)**:
  - Lựa chọn kích thước khe lọc (slot size) quá lớn so với thành phần hạt cát của tầng chứa nước.
  - Cấp phối sỏi lọc nhân tạo sai quy cách, tạo khoảng hở cho cát mịn chui qua.
  - Vận tốc dòng vào khe lọc vượt quá giới hạn an toàn ($v_{\text{entrance}} > 0.03\text{ m/s}$), lực kéo thủy động thắng lực trọng trường làm hóa lỏng cát tầng chứa.
  - Rách vỡ cơ học hoặc ăn mòn thủng thân ống lọc do địa chấn sụt lún vách giếng.
- **Biện pháp kỹ thuật khắc phục (Remedial Engineering Actions)**:
  1. Thả camera chuyên dụng nội soi kiểm tra lòng giếng (Downhole CCTV Camera Inspection) để tìm chính xác vị trí ống lọc bị rách thủng.
  2. Điều tiết van đóng bớt lưu lượng bơm để hạ vận tốc dòng vào khe về ngưỡng an toàn $v_{\text{entrance}} \le 0.03\text{ m/s}$.
  3. Nếu ống lọc bị rách: Thi công thả ống lót lọc mới (Screen liner sleeve) có đường kính nhỏ hơn kèm chèn sỏi mịn đặt bên trong lòng ống lọc cũ để bịt kín đoạn hỏng.

##### 2.6.2.2 Hiện Tượng Đóng Cặn Hóa Học và Khoáng Hóa Khe Lọc (Screen Chemical Incrustation & Mineral Scaling)
- **Mã sự cố**: `tb_ch02_04`
- **Triệu chứng nhận biết (Symptoms)**:
  - Năng suất riêng ($\text{SC} = Q/s_w$) của giếng khoan suy giảm liên tục qua các tháng/năm.
  - Mực nước tĩnh ($H_0$) không thay đổi nhưng mực nước động ($PWL$) tụt sâu bất thường, điện năng tiêu thụ trên một mét khối nước tăng cao.
- **Nguyên nhân gốc rễ (Root Causes)**:
  - Vận tốc nước qua khe lọc cao gây sụt áp cục bộ, làm thoát khí $\text{CO}_2$ tự do hòa tan, phá vỡ cân bằng cacbonat:
    $$\text{Ca}(\text{HCO}_3)_2 \rightarrow \text{CaCO}_3\downarrow + \text{CO}_2\uparrow + \text{H}_2\text{O}$$
    Tạo ra kết tủa Canxi cacbonat dạng đá vôi rắn bám cứng bịt kín các khe hở và lỗ rỗng của tầng sỏi lọc.
  - Sự xâm nhập của oxy từ trên mặt giếng oxy hóa ion sắt hai ($\text{Fe}^{2+}$) và mangan hai ($\text{Mn}^{2+}$) thành kết tủa sắt ba hydroxit $\text{Fe}(\text{OH})_3$ và mangan dioxit $\text{MnO}_2$ nhầy nhớt bám chặt vào lưới lọc; sự phát triển của vi khuẩn sắt (*Gallionella*, *Sphaerotilus*).
- **Biện pháp kỹ thuật khắc phục (Remedial Engineering Actions)**:
  1. Tẩy rửa phục hồi giếng bằng hóa chất (Chemical Well Rehabilitation): Bơm dung dịch axit clohydric ($\text{HCl}$) ức chế ăn mòn nồng độ $15\% - 20\%$ hoặc axit sulfamic ($\text{H}_3\text{NSO}_3$) trộn hóa chất hoạt tính bề mặt vào vùng ống lọc. Ngâm ủ trong $12 - 24\text{ giờ}$ để hòa tan toàn bộ cặn đá vôi và oxit sắt.
  2. Kết hợp cơ học: Dùng cần khoan gắn bàn chải thép chải sạch khe lọc và sục sạo bằng pít-tông kéo giật xung lực.
  3. Bơm xả kiệt toàn bộ cặn hóa chất ra khỏi giếng cho đến khi nước đạt độ $\text{pH}$ trung tính và sạch cặn trước khi cấp trở lại mạng lưới.

##### 2.6.2.3 Hiện Tượng Tụt Mực Nước Động và Xâm Thực Bơm Khai Thác (Dynamic Drawdown & Pump Cavitation)
- **Mã sự cố**: `tb_ch02_05`
- **Triệu chứng nhận biết (Symptoms)**:
  - Bơm chìm phát ra tiếng nổ lách tách như bắn sỏi, rung giật rung lắc đường ống đẩy.
  - Lưu lượng nước cấp lên nhà máy giảm sút đột ngột; dòng điện động cơ dao động chập chờn.
- **Nguyên nhân gốc rễ (Root Causes)**:
  - Khai thác quá mức trong mùa khô khiến mực nước động ($PWL$) tụt sâu xuống thấp hơn vị trí lắp đặt miệng hút của bơm chìm, khiến bơm hút lẫn bọt khí.
  - Đối với bơm đặt cạn: Mực nước động tụt sâu vượt quá chiều cao hút tĩnh cho phép ($h_{\text{lift}} > h_{\text{suction, max}} \approx 7.0\text{ m}$).
- **Biện pháp kỹ thuật khắc phục (Remedial Engineering Actions)**:
  1. Khẩn cấp: Tắt bơm hoặc điều tiết van xả giảm lưu lượng khai thác.
  2. Nối dài thêm các đoạn ống đẩy (column pipes) để hạ sâu vị trí treo bơm chìm xuống dưới mực nước động kiệt tối thiểu $3.0 - 5.0\text{ m}$ (nhưng phải cao hơn đỉnh ống lọc tối thiểu $1.0\text{ m}$ để dòng nước làm mát vỏ động cơ đúng kỹ thuật).
  3. Đối với giếng nông dùng bơm cạn: Thay thế toàn bộ cụm bơm đặt cạn bằng máy bơm chìm thả đáy.

##### 2.6.2.4 Hiện Tượng Xâm Nhập Mặn và Nón Mặn Dâng Cao (Saltwater Intrusion & Saline Upconing)
- **Mã sự cố**: `tb_ch02_06`
- **Triệu chứng nhận biết (Symptoms)**:
  - Độ dẫn điện ($\text{EC}$) và tổng chất rắn hòa tan ($\text{TDS}$) của nước giếng tăng đột biến.
  - Hàm lượng Clorua ($\text{Cl}^-$) vượt ngưỡng tiêu chuẩn quy chuẩn sinh hoạt ($> 250\text{ mg/L}$), nước có vị lợ mặn.
- **Nguyên nhân gốc rễ (Root Causes)**:
  - Khai thác nước ngầm quá mức (over-pumping) tại các dải đồng bằng ven biển (như bán đảo Cà Mau, Đồng bằng sông Cửu Long, hoặc dải ven biển miền Trung).
  - Phá vỡ thế cân bằng thủy tĩnh tự nhiên Ghyben-Herzberg giữa nước ngọt và nước mặn:
    $$z = \frac{\rho_f}{\rho_s - \rho_f} \cdot h_f \approx 40 \cdot h_f$$
    *(Cứ mỗi mét mực nước ngọt bị hạ thấp, nêm nước mặn bên dưới sẽ dâng cao lên $40\text{ m}$ theo hình nón mặn - Saline Upconing chui thẳng vào đáy ống lọc giếng khoan).*
- **Biện pháp kỹ thuật khắc phục (Remedial Engineering Actions)**:
  1. Cắt giảm ngay lưu lượng khai thác của giếng hoặc dừng hoạt động luân phiên.
  2. Cắt bỏ đoạn ống lọc ở phần đáy sâu của giếng, trám vữa xi măng bịt đáy để chỉ thu nước ở phần trên của tầng chứa nước ngọt.
  3. Tái cấu trúc quy hoạch bãi giếng: Di dời các giếng sâu vào sâu trong nội địa cách xa đường bờ biển; triển khai giải pháp bổ cập nhân tạo tầng chứa nước (Managed Aquifer Recharge - MAR) bằng cách bơm ép nước mưa hoặc nước mặt đã xử lý ngược vào lòng đất để tái tạo áp lực đẩy lùi nêm mặn.

---

### 2.7 Khung Tiêu Chuẩn Kỹ Thuật và Quy Chuẩn Thiết Kế Hiện Hành (Regulatory Standards Framework)
#### 2.7.1 Tiêu Chuẩn Thiết Kế Công Trình Cấp Nước TCXDVN 33:2006 / TCVN 33:2006
**TCXDVN 33:2006 / TCVN 33:2006** - *Cấp nước - Mạng lưới đường ống và công trình - Tiêu chuẩn thiết kế* (Bộ Xây dựng ban hành) là quy chuẩn kỹ thuật bắt buộc áp dụng trong thiết kế công trình thu nước tại Việt Nam (`reg_ch02_01`):

| Hạng Mục Kỹ Thuật | Thông Số Quy Định Bắt Buộc | Căn Cứ Điều Khoản & Mục Đích Kỹ Thuật |
| :--- | :--- | :--- |
| **Vận tốc cửa vào công trình thu nước mặt** | $v_{\text{port}} = 0.15 - 0.30\text{ m/s}$ (nước hồ); $v \le 0.15\text{ m/s}$ (lưới chắn) | Điều 4.2: Bảo vệ sinh vật thủy sinh, cá con và ngăn ngừa rác nổi. |
| **Vận tốc đường ống tự chảy/xi-phông** | $v = 0.60 - 1.50\text{ m/s}$ (tự chảy); $v \ge 0.60\text{ m/s}$ | Điều 4.6: Chống lắng cặn hạt phù sa mịn trong ống ngầm đáy sông. |
| **Khoảng cách song chắn rác thô** | $b = 40 - 50\text{ mm}$ (cơ giới); $b = 25 - 40\text{ mm}$ (thủ công) | Điều 4.8: Ngăn chặn rác kích thước lớn bảo vệ máy bơm và lưới tinh. |
| **Kích thước mắt lưới chắn rác tinh** | $b_{\text{mesh}} = 2 - 10\text{ mm}$ (tiêu chuẩn $5 - 6\text{ mm}$) | Điều 4.9: Chắn rác nhỏ, bèo, rong rêu trước khi vào ngăn hút trạm bơm. |
| **Vận tốc dòng vào khe ống lọc giếng khoan** | $v_{\text{screen}} \le 0.03\text{ m/s}$ ($30\text{ mm/s} = 0.1\text{ ft/s}$) | Điều 4.16: Chống đùn cát tầng chứa, triệt tiêu tổn thất cột áp và đóng cặn. |
| **Độ sâu trám vữa xi măng bảo vệ giếng** | $z_{\text{grout}} \ge 5 - 10\text{ m}$ (chuẩn $10 - 15\text{ m}$) | Điều 4.18: Cách ly vệ sinh tuyệt đối bề mặt và các tầng nước nông ô nhiễm. |
| **Vùng bảo hộ vệ sinh nguồn nước cấp I** | Bán kính $100 - 200\text{ m}$ (nước mặt); $30 - 50\text{ m}$ (giếng ngầm) | Điều 11.2: Vùng bảo vệ nghiêm ngặt, rào chắn kiên cố, cấm mọi xâm phạm. |
| **Vùng bảo hộ vệ sinh nguồn nước cấp II** | Bán kính $1,000 - 2,000\text{ m}$ thượng lưu; $300 - 500\text{ m}$ quanh giếng | Điều 11.3: Hạn chế ô nhiễm, cấm xả thải chưa xử lý, cấm kho chứa hóa chất. |

#### 2.7.2 Quy Chuẩn Kỹ Thuật Quốc Gia Về Chất Lượng Nước Sạch Sinh Hoạt QCVN 01-1:2018/BYT
**QCVN 01-1:2018/BYT** do Bộ Y tế ban hành quy định giới hạn các thông số chất lượng đối với nước sạch sử dụng cho mục đích sinh hoạt (`reg_ch02_02`):

| Chỉ Số Chất Lượng Nước | Đơn Vị Đo | Ngưỡng Giới Hạn Tối Đa Cho Phép | Ý Nghĩa Kỹ Thuật Liên Quan Đến Công Trình Thu |
| :--- | :--- | :--- | :--- |
| **Độ đục (Turbidity)** | $\text{NTU}$ | $\le 2.0$ (tại vòi tiêu dùng) | Quyết định công nghệ thu: RBF lọc ven bờ đưa độ đục về $< 1\text{ NTU}$. |
| **Màu sắc (Color)** | $\text{TCU}$ | $\le 15.0$ | Tránh thu tầng mặt hồ chứa giàu chất mùn hữu cơ humic/fulvic. |
| **Độ pH** | $-$ | $6.0 - 8.5$ | pH nước ngầm $< 6.0$ gây ăn mòn kim loại ống lọc và cánh bơm giếng. |
| **Tổng độ cứng (Total Hardness)** | $\text{mg/L as }\text{CaCO}_3$ | $\le 300.0$ | Nước ngầm tầng đá vôi thường có độ cứng cao, gây đóng cặn khe lọc. |
| **Hàm lượng Sắt tổng ($\text{Fe}$)** | $\text{mg/L}$ | $\le 0.30$ | Sắt hai tầng đáy gây tắc nghẹt sinh học do vi khuẩn sắt tạo màng nhầy. |
| **Hàm lượng Mangan tổng ($\text{Mn}$)** | $\text{mg/L}$ | $\le 0.10$ | Tránh hút nước yếm khí tầng hypolimnion đáy hồ giàu mangan hòa tan. |
| **Clorua ($\text{Cl}^-$)** | $\text{mg/L}$ | $\le 250.0$ | Chỉ thị trực tiếp của xâm nhập mặn; vượt ngưỡng phải đóng giếng khẩn cấp. |
| **Vi khuẩn E. coli / Coliform tổng** | $\text{CFU}/100\text{ mL}$ | Không phát hiện ($0$) | Nước giếng nông bị nhiễm vi sinh nếu sân giếng không đạt chuẩn vệ sinh. |

#### 2.7.3 Quy Chuẩn Chất Lượng Nước Mặt QCVN 08:2023/BTNMT & Tiêu Chuẩn Quốc Tế US EPA 316(b)
- **QCVN 08:2023/BTNMT** (Bộ Tài nguyên và Môi trường ban hành, `reg_ch02_03`): Xác lập ngưỡng chất lượng nước mặt cho mục đích cấp nước sinh hoạt: $\text{BOD}_5 \le 4\text{ mg/L}$, $\text{COD} \le 10\text{ mg/L}$, $\text{TOC} \le 4\text{ mg/L}$, $\text{DO} \ge 5\text{ mg/L}$, $\text{NH}_4^+ \le 0.3\text{ mg/L}$. Định hướng vị trí thu nước mặt phải luôn nằm trong các đoạn sông hoặc vùng hồ đạt tối thiểu phân hạng A.
- **US EPA 316(b) Clean Water Act**: Tiêu chuẩn tham chiếu quốc tế bắt buộc về bảo vệ hệ sinh thái thủy sinh tại công trình thu: Khống chế vận tốc tiếp cận xuyên qua mắt lưới $v_{\text{through-screen}} \le 0.5\text{ ft/s}$ ($0.15\text{ m/s}$), kết hợp hệ thống máng trượt giải cứu cá con (fish return trough) để đưa sinh vật quay trở lại dòng sông an toàn không bị tổn thương.
