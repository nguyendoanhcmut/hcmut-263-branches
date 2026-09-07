## Chương 05.2: Xử lý Sinh học - Quá trình Bùn hoạt tính & Sinh thái Vi sinh (Biological Treatment - Activated Sludge & Microbial Ecology)

### 1. Hệ sinh thái và Cấu trúc Quần xã Vi sinh vật trong Bùn hoạt tính (Activated Sludge Ecosystem & Microbial Community Ecology)

#### 1.1 Cấu trúc vi mô của Bông bùn sinh học (Bio-floc Microstructure & Extracellular Polymeric Substances - EPS)

##### 1.1.1 Thành phần hóa sinh và Cơ chế kết tụ tạo bông (Biochemical Composition & Flocculation Mechanisms)

###### 1.1.1.1 Polyme ngoại bào (Extracellular Polymeric Substances - EPS) và Khung xương cấu trúc
- **Khái niệm và Nguồn gốc sinh học:**
  - EPS là mạng lưới đại phân tử cao phân tử do vi khuẩn tổng hợp và tiết ra ngoài màng tế bào trong quá trình trao đổi chất, hoặc giải phóng từ quá trình tự phân hủy nội sinh (cell lysis).
  - Phân bố EPS gồm hai dạng:
    - *Soluble EPS / Slime*: Polyme hòa tan, liên kết lỏng lẻo với bề mặt tế bào, dễ khuếch tán vào pha lỏng làm tăng độ nhớt môi trường.
    - *Bound EPS*: Polyme liên kết chặt, gồm hai lớp: lớp khuếch tán lỏng lẻo bên ngoài (*Loosely Bound EPS - LB-EPS*) và lớp gắn kết chặt chẽ bên trong (*Tightly Bound EPS - TB-EPS*).
- **Thành phần hóa sinh định lượng:**
  - *Polysaccharides* ($40 - 60\%$ tổng lượng EPS): Cung cấp các nhóm chức phân cực hydroxyl ($-\text{OH}$), carboxyl ($-\text{COOH}$), tạo liên kết hydro và cấu trúc gel ngậm nước.
  - *Proteins* ($20 - 40\%$ tổng lượng EPS): Chứa các acid amin phân cực và kỵ nước, quyết định tính chất bề mặt, điểm đẳng điện (isoelectric point) và khả năng tạo liên kết cộng hóa trị/phối trí.
  - *Acid nucleic* (DNA/RNA ngoại bào, $e\text{DNA} \approx 5 - 10\%$): Hoạt động như chất kết dính sinh học thứ cấp, tăng cường độ bền cơ học cho bông bùn.
  - *Lipids và Acid humic* ($5 - 15\%$): Tăng cường tương tác kỵ nước giữa các vi khuẩn.
- **Thuyết Cầu nối Cation Đa hóa trị (Divalent Cation Bridging Theory - DCBT):**
  - Bề mặt màng tế bào vi khuẩn và các phân tử EPS mang điện tích âm thuần ở dải $\text{pH}$ trung tính ($6.5 - 8.0$) do sự ion hóa của các nhóm carboxyl ($-\text{COO}^-$) và phosphate ($-\text{PO}_4^{3-}$).
  - Các cation hóa trị hai, điển hình là $\text{Ca}^{2+}$ và $\text{Mg}^{2+}$, đóng vai trò là "cầu nối tĩnh điện" liên kết các nhóm mang điện tích âm của chuỗi polyme liền kề:
    $$-\text{COO}^- \cdots \text{Ca}^{2+} \cdots ^-\text{OOC}-$$
  - Ngưỡng tỷ lệ tối ưu trong nước thải:
    $$\frac{[\text{Ca}^{2+}] + [\text{Mg}^{2+}]}{[\text{Na}^+] + [\text{K}^+]} > 1.0 - 2.0 \quad (\text{tính theo đương lượng mol } meq/L)$$
  - Nếu tỷ số cation đơn hóa trị ($\text{Na}^+, \text{K}^+, \text{NH}_4^+$) vượt trội ($\text{ratio} < 1.0$), hiện tượng trao đổi ion sẽ thế chỗ $\text{Ca}^{2+}/\text{Mg}^{2+}$, phá vỡ cầu nối cation, dẫn đến hiện tượng rã bông bùn (*floc deterioration*), làm tăng độ đục nước sau lắng.

###### 1.1.1.2 Cân bằng lực keo tụ sinh học: Thuyết DLVO mở rộng và Tương tác kỵ nước
- **Mô hình tương tác keo tụ (Extended DLVO Theory):**
  - Tổng năng lượng tương tác giữa hai tế bào vi sinh vật $V_{\text{total}}$ là hàm số của khoảng cách phân cách $h$:
    $$V_{\text{total}}(h) = V_A(h) + V_R(h) + V_{\text{hyd}}(h) + V_{\text{steric}}(h)$$
  - Trong đó:
    - $V_A(h)$: Năng lượng hút van der Waals (lực hút tầm xa):
      $$V_A(h) = -\frac{A_H \cdot d_p}{24 h}$$
      ($A_H$ là hằng số Hamaker $\approx 10^{-20}\ \text{J}$, $d_p$ là đường kính tế bào $\approx 1.0\ \mu\text{m}$).
    - $V_R(h)$: Năng lượng đẩy tĩnh điện lớp điện kép (electrostatic double layer repulsion):
      $$V_R(h) = 2\pi \varepsilon_0 \varepsilon_r d_p \psi_0^2 \ln(1 + e^{-\kappa h})$$
      ($\varepsilon_0$ là hằng số điện môi chân không, $\varepsilon_r$ là hằng số điện môi nước, $\psi_0$ là thế bề mặt xấp xỉ điện thế Zeta $\zeta \approx -15 \text{ đến } -30\ \text{mV}$, $\kappa$ là nghịch đảo chiều dày lớp điện kép Debye-Hückel).
    - $V_{\text{hyd}}(h)$: Tương tác kỵ nước/ưa nước sinh học (Hydrophobic interaction energy). Khi vi khuẩn già đi (pha phân hủy nội sinh), bề mặt tế bào tổng hợp nhiều hợp chất kỵ nước, $V_{\text{hyd}}$ âm mạnh, kéo các tế bào lại gần nhau vượt qua hàng rào năng lượng đẩy $V_R$.
    - $V_{\text{steric}}(h)$: Lực cản lập thể (Steric repulsion) do các chuỗi polymer EPS cồng kềnh va chạm khi hai bề mặt tiếp cận ở cự ly $< 2 - 5\ \text{nm}$.
- **Động học keo tụ sinh học:**
  - Ở pha tăng trưởng hàm mũ (Exponential phase), tỷ số thức ăn trên vi sinh vật ($F/M$) cao, vi khuẩn linh động, tổng hợp EPS chưa đủ liên kết, thế Zeta âm cao $\rightarrow$ vi khuẩn phân tán rời rạc (*dispersed growth*).
  - Ở pha suy tàn/nội sinh (Endogenous phase), $F/M$ thấp ($0.2 - 0.5\ \text{d}^{-1}$), điện thế Zeta giảm (về gần $-10\ \text{mV}$), EPS cô đặc và các protein kỵ nước bộc lộ $\rightarrow$ keo tụ sinh học tự phát diễn ra triệt để, tạo bông bùn có đường kính $100 - 500\ \mu\text{m}$.

##### 1.1.2 Vi khuẩn tạo bông chính (Floc-Forming Bacteria)

###### 1.1.2.1 *Zoogloea ramigera* và Cơ chế tiết nang chất nhờn (Zoogloeal Gel Matrix)
- **Đặc điểm hình thái và phân loại:**
  - Trực khuẩn Gram âm, hiếu khí bắt buộc, có khả năng chuyển động nhờ lông roi cực (polar flagellum) ở trạng thái đơn lẻ.
  - Phân loại học: Thuộc lớp *Betaproteobacteria*, bộ *Rhodocyclales*, họ *Rhodocyclaceae*.
- **Cơ chế sinh lý học và Tạo nang keo:**
  - Khi môi trường dư thừa cacbon hữu cơ nhưng giới hạn nitơ hoặc chuyển sang pha ổn định, *Zoogloea ramigera* tiết ra một lượng lớn exopolysaccharide ngoại bào dạng gel phân nhánh phức tạp (gồm glucose, galactose, acid glucuronic).
  - Tích lũy cơ chất nội bào dạng Poly-$\beta$-hydroxybutyrate (PHB) làm nguồn năng lượng dự trữ:
    $$n\ \text{Ac-CoA} \rightarrow \text{Acetoacetyl-CoA} \rightarrow \text{3-hydroxybutyryl-CoA} \rightarrow (\text{C}_4\text{H}_6\text{O}_2)_n\ (\text{PHB})$$
  - Các tế bào vi khuẩn nằm vùi sâu bên trong khối chất nền gelatin dày đặc hình ngón tay hoặc hình cành cây (*finger-like / dendritic zoogloeal colonies*).
  - Khối chất nền này bảo vệ vi khuẩn khỏi tác động của lực cắt thủy lực cao và sự tấn công của các chất độc hại, đồng thời cung cấp diện tích bề mặt lớn hấp phụ các chất keo hữu cơ trong nước thải.

###### 1.1.2.2 Các chủng vi khuẩn tạo bông đồng hành (*Pseudomonas*, *Achromobacter*, *Flavobacterium*, *Alcaligenes*)
- ***Pseudomonas* spp.:**
  - Trực khuẩn Gram âm, hóa dị dưỡng linh hoạt, tiết alginate ngoại bào tạo cấu trúc vi mô vững chắc cho bông bùn.
  - Khả năng dị hóa mạnh các hợp chất hydrocacbon thơm, phenol, acid béo và tham gia khử nitrat khi xuất hiện điều kiện thiếu khí cục bộ bên trong lõi bông bùn.
- ***Flavobacterium* spp.:**
  - Gram âm, sắc tố vàng/cam, chuyên biệt phân hủy các polyme sinh học phức tạp như protein, pectin, tinh bột thành các monomer dễ hấp thu.
- ***Alcaligenes* và *Achromobacter* spp.:**
  - Trực khuẩn Gram âm, có khả năng oxy hóa các acid hữu cơ mạch ngắn và thực hiện khử nitrat đồng thời trong điều kiện vi hiếu khí (micro-aerophilic).

---

#### 1.2 Vi sinh vật dạng sợi (Filamentous Organisms) và Vai trò Cốt lõi trong Bùn hoạt tính

##### 1.2.1 Cấu trúc "Cốt thép - Bê tông" (Backbone Hypothesis)

###### 1.2.1.1 Vai trò tích cực của vi khuẩn dạng sợi ở mật độ tối ưu
- **Thuyết Khung xương (Backbone Model - Sezgin et al.):**
  - Bông bùn hoạt tính lý tưởng được ví như một cấu trúc "bê tông cốt thép" trong xây dựng công trình:
    - *Cốt thép*: Các sợi vi khuẩn dạng filament mảnh dài đan xen chéo nhau tạo thành mạng lưới khung ba chiều (structural backbone).
    - *Bê tông*: Các khuẩn lạc vi khuẩn tạo bông (*Zoogloea*, *Pseudomonas*) cùng với gel EPS kết dính lấp đầy các khoảng trống giữa các thanh cốt thép sợi.
- **Lợi ích cơ học và công nghệ:**
  - Tăng cường độ bền chịu cắt thủy lực ($G > 50 - 100\ \text{s}^{-1}$), ngăn ngừa hiện tượng vỡ vụn bông bùn trong đường ống dẫn và bể lắng.
  - Tạo kích thước bông bùn lớn ($d_f = 200 - 500\ \mu\text{m}$), nâng cao vận tốc lắng trọng lực theo định luật Stokes cải tiến.
  - Hỗ trợ lọc các hạt cặn siêu mịn và vi khuẩn phân tán khi ranh giới bùn hạ xuống trong quá trình lắng khối (zone settling).

###### 1.2.1.2 Hậu quả khi mất cân bằng mật độ vi khuẩn dạng sợi
- **Mật độ sợi quá thấp (Filament-deficient / Pin-point floc):**
  - Thiếu khung giằng cơ học $\rightarrow$ bông bùn nhỏ mịn ($d_f < 50 - 100\ \mu\text{m}$), hình cầu đặc, yếu ớt.
  - Mặc dù lắng nhanh nhưng không giữ được các hạt nhỏ lơ lửng $\rightarrow$ nước trong sau lắng có độ đục cao ($TSS_e > 30\ \text{mg/L}$).
- **Mật độ sợi phát triển quá mức (Filamentous Bulking):**
  - Các sợi vi khuẩn phát triển vượt ra khỏi bề mặt ngoài của bông bùn, vươn dài tự do vào pha lỏng ($L_{\text{filament}} > 10^7\ \mu\text{m/mL}$ mixed liquor).
  - Các sợi vươn ra ngăn cản các bông bùn tiếp cận và nén chặt vào nhau (*bridging effect*), tạo thể tích rỗng xốp khổng lồ, khiến chỉ số thể tích bùn tăng vọt ($SVI > 150 - 300\ \text{mL/g}$), đe dọa trào bùn ra ngoài theo máng thu.

##### 1.2.2 Phân loại và Đặc tính sinh lý của các nhóm vi khuẩn dạng sợi chủ yếu

###### 1.2.2.1 *Sphaerotilus natans* (Sewage Fungus)
- **Hình thái và Phản ứng nhuộm:**
  - Sợi dài thẳng hoặc uốn lượn nhẹ ($100 - 500\ \mu\text{m}$), chiều rộng tế bào $1.2 - 2.5\ \mu\text{m}$, chiều dài tế bào $3 - 8\ \mu\text{m}$.
  - Nằm trong một vỏ bọc màng gelatin hình ống rõ rệt (*tubular sheath*).
  - Phản ứng nhuộm: Gram âm ($\text{Gram}^-$), Neisser âm ($\text{Neisser}^-$), không có hạt lưu huỳnh nội bào.
  - Phân loại học: *Betaproteobacteria*, bộ *Burkholderiales*, họ *Comamonadaceae*.
- **Đặc tính sinh thái và Động học phát triển:**
  - Hằng số nửa bão hòa oxy hòa tan rất thấp:
    $$K_{O2, \text{S.natans}} \approx 0.05 - 0.10\ \text{mg/L} \quad (\text{so với vi khuẩn tạo bông } K_{O2, \text{floc}} \approx 0.20 - 0.50\ \text{mg/L})$$
  - Ưu thế cạnh tranh: Ở nồng độ $DO < 1.0\ \text{mg/L}$ trong các bể hiếu khí hoàn toàn xáo trộn (CMAS) hoặc nồng độ đường đơn/axit hữu cơ cao, *S. natans* sinh trưởng áp đảo vi khuẩn tạo bông, gây phình bùn nghiêm trọng.

###### 1.2.2.2 *Microthrix parvicella*
- **Hình thái và Phản ứng nhuộm:**
  - Sợi mảnh, cuộn xoắn rối bùi nhùi như búi len nằm sâu trong hoặc vươn nhẹ ngoài bông bùn. Đường kính sợi cực nhỏ ($0.6 - 0.8\ \mu\text{m}$), chiều dài $50 - 200\ \mu\text{m}$, không có vỏ bao sheath.
  - Phản ứng nhuộm: Gram dương ($\text{Gram}^+$), Neisser dương từng đoạn hoặc toàn bộ ($\text{Neisser}^+$), tạo hạt polyphosphate đậm đặc.
- **Đặc tính sinh lý và Cơ chế chọn lọc:**
  - Sinh vật kỵ khí tùy nghi/vi hiếu khí, có khả năng hấp thu và tích lũy trực tiếp các Acid béo mạch dài (Long-Chain Fatty Acids - LCFA, ví dụ oleic acid, palmitic acid) mà không cần năng lượng vận chuyển chủ động ban đầu.
  - Ưu thế đặc biệt ở nhiệt độ nước thải thấp ($T < 12 - 15^\circ\text{C}$) và tuổi bùn dài ($SRT > 10 - 20\ \text{ngày}$), hệ thống thiếu khí xen kẽ hiếu khí (bể BNR khử N & P).
  - Sinh tổng hợp lipid màng kỵ nước, là nguyên nhân kép gây ra cả **Phình bùn** và **Bọt sinh học nhớt màu nâu** trên bể lắng và bể hiếu khí.

###### 1.2.2.3 *Thiothrix* spp. và Vi sinh vật oxy hóa lưu huỳnh (Sulfur-Oxidizing Filaments: *Beggiatoa*, Type 021N)
- **Hình thái và Phản ứng nhuộm:**
  - *Thiothrix* spp.: Sợi thẳng hoặc hơi uốn, có gốc đính (holdfast) hình hoa thị (rosettes) và giải phóng các tế bào di động dạng gonidia. Tế bào hình chữ nhật ($0.8 - 2.5\ \mu\text{m} \times 2 - 5\ \mu\text{m}$).
  - Type 021N: Sợi không có vỏ bọc, dạng chuỗi hạt tế bào hình thùng (barrel-shaped cells), thắt eo tại vách ngăn giữa các tế bào.
  - Phản ứng nhuộm: $\text{Gram}^-$, $\text{Neisser}^-$. Khi thử nghiệm phản ứng oxy hóa sulfur ($S$-test), tế bào chứa đầy các hạt lưu huỳnh nguyên tố ($S^0$) nội bào khúc xạ ánh sáng lấp lánh dưới kính hiển vi quang học pha tương phản (phase-contrast).
- **Ý nghĩa chỉ thị môi trường:**
  - Chỉ thị rõ nét hiện tượng **nước thải bị nhiễm thối / lưu cữu (septic wastewater)** sinh ra hydro sulfide ($H_2S, HS^-$) từ mạng lưới cống thu gom hoặc bể tự hoại.
  - Sử dụng $H_2S$ làm chất cho electron để tạo năng lượng:
    $$2\text{H}_2\text{S} + \text{O}_2 \rightarrow 2\text{S}^0 + 2\text{H}_2\text{O} \quad (\text{tích lũy hạt } S^0)$$
    $$2\text{S}^0 + 3\text{O}_2 + 2\text{H}_2\text{O} \rightarrow 2\text{SO}_4^{2-} + 4\text{H}^+ \quad (\text{khi hết } H_2S)$$
  - Phát triển cực thịnh khi nước thải thiếu chất dinh dưỡng Nitơ và Phospho ($BOD_5 : N : P \ll 100 : 5 : 1$).

###### 1.2.2.4 *Haliscomenobacter hydrossis* và các chủng Eikelboom (Type 0041, 0092, 0675, 1701, 1851)
- ***Haliscomenobacter hydrossis*:**
  - Sợi cực mảnh ($0.3 - 0.5\ \mu\text{m}$), thẳng như kim khâu, cắm tủa tủa từ tâm bông bùn ra ngoài như gai nhím.
  - Chỉ thị điển hình của nồng độ DO thấp ($< 1.0\ \text{mg/L}$) trong các hệ thống aerotank xáo trộn hoàn toàn.
- **Eikelboom Type 0041 và Type 0675:**
  - Trực khuẩn dạng sợi có vỏ bao dày, trên bề mặt bám dính dày đặc các vi khuẩn biểu sinh (epiphytic bacteria).
  - Phản ứng nhuộm: Gram thay đổi ($\text{Gram}^{+/-}$), Neisser dương ở vỏ bao.
  - Chỉ thị môi trường tải lượng hữu cơ cực thấp ($F/M < 0.1\ \text{d}^{-1}$), thời gian lưu bùn dài ($SRT > 15 - 30\ \text{ngày}$), hoặc nước thải chứa nhiều hợp chất hữu cơ chậm phân hủy.
- **Eikelboom Type 1701:**
  - Tế bào hình bầu dục nằm trong vỏ bọc lỏng lẻo, bám dày đặc vi khuẩn biểu sinh.
  - Chỉ thị tuyệt đối của tình trạng **thiếu hụt oxy hòa tan nghiêm trọng** kết hợp với $F/M$ từ thấp đến trung bình.

---

#### 1.3 Động vật nguyên sinh (Protozoa) và Động vật đa bào (Metazoa) làm Chỉ thị sinh học (Bio-Indicators)

##### 1.3.1 Trùng lông (Ciliates) - Chỉ thị cho Hệ thống Ổn định và Nước đầu ra Chất lượng Tốt

###### 1.3.1.1 Trùng lông có cuống (Stalked Ciliates: *Vorticella*, *Carchesium*, *Opercularia*, *Epistylis*)
- **Hình thái học và Sinh thái:**
  - Cơ thể hình chuông hoặc chiếc loa, gắn cố định vào bông bùn bằng một cuống co rút được (*Vorticella*, cuống có dải cơ myoneme) hoặc cuống phân nhánh không co rút (*Epistylis*, *Carchesium*).
  - Miệng loe rộng có vành lông rung (cilia) đập liên tục tạo dòng xoáy thủy lực cuốn các vi khuẩn tự do phân tán, hạt keo hữu cơ vào bào khẩu.
- **Vai trò xử lý và Chỉ thị công nghệ:**
  - *Lọc sạch nước*: Tiêu thụ vi khuẩn tự do phân tán ($10^3 - 10^4\ \text{vi khuẩn/cá thể}\cdot\text{h}$), làm giảm đột biến độ đục và chỉ số $TSS$ của nước sau lắng.
  - *Chỉ thị sinh học*: Báo hiệu hệ thống bùn hoạt tính hoạt động ở trạng thái **trưởng thành, vận hành ổn định**, tuổi bùn cân bằng ($SRT \approx 5 - 12\ \text{ngày}$), nồng độ oxy hòa tan đầy đủ ($DO \ge 2.0\ \text{mg/L}$), hiệu suất khử BOD đạt $> 90\%$.
  - Nếu trùng lông có cuống co cụm thân lại, không mở vành lông, hoặc xuất hiện bọc kén (encystment) $\rightarrow$ dấu hiệu nước thải có độc chất (kim loại nặng, hóa chất khử trùng) hoặc thiếu oxy cấp tính.

###### 1.3.1.2 Trùng lông bò (Crawling / Grazing Ciliates: *Aspidisca*, *Euplotes*)
- **Hình thái và Hành vi:**
  - Cơ thể dẹt lưng bụng, các lông rung phía bụng liên kết thành các gai cứng di chuyển (cirri), cho phép chúng "bò" và gặm nhấm trên bề mặt các bông bùn hoạt tính.
  - Điển hình: *Aspidisca cicada* (kích thước $30 - 50\ \mu\text{m}$).
- **Ý nghĩa sinh thái:**
  - Chỉ thị quá trình làm sạch đạt mức độ cao, bùn có đặc tính kết tụ và lắng nén xuất sắc ($SVI = 80 - 120\ \text{mL/g}$).
  - Kích thích vi khuẩn tiết thêm EPS tươi để tái tạo bề mặt bông bùn, hỗ trợ quá trình nitrat hóa diễn ra thuận lợi.

###### 1.3.1.3 Trùng lông bơi tự do (Free-Swimming Ciliates: *Paramecium*, *Colpidium*, *Tetrahymena*)
- **Hình thái và Phân bố:**
  - Cơ thể hình đế giày hoặc hình trứng, toàn thân bao phủ bởi các hàng lông rung nhịp nhàng, bơi lội tự do trong pha nước giữa các bông bùn.
- **Ý nghĩa công nghệ:**
  - Chiếm ưu thế ở giai đoạn chuyển tiếp giữa tải lượng hữu cơ trung bình và cao ($F/M \approx 0.3 - 0.6\ \text{d}^{-1}$), hoặc hệ thống đang trong giai đoạn hồi phục sau sự cố sốc tải.

##### 1.3.2 Trùng roi (Flagellates) và Trùng amip (Amoebae) - Chỉ thị Hệ thống Khởi động hoặc Quá tải Hữu cơ

###### 1.3.2.1 Trùng roi (*Flagellates*: *Bodo*, *Monas*, *Trepomonas*, *Hexamitus*)
- **Đặc điểm sinh học:**
  - Kích thước hiển vi rất nhỏ ($5 - 20\ \mu\text{m}$), chuyển động xoay tròn hoặc giật cục nhờ 1 đến 4 roi (flagella).
  - Có khả năng hấp thu trực tiếp chất hữu cơ hòa tan qua màng (osmotrophic nutrition) bên cạnh việc bắt vi khuẩn.
- **Ý nghĩa chỉ thị công nghệ:**
  - Chiếm số lượng áp đảo khi **tải lượng hữu cơ quá cao ($F/M > 0.6 - 1.0\ \text{d}^{-1}$)**, bùn non ($SRT < 2 - 3\ \text{ngày}$), quá trình xử lý chưa hoàn tất.
  - Phổ biến trong giai đoạn bắt đầu khởi động (start-up) trạm xử lý hoặc khi bể hiếu khí bị sốc tải hữu cơ đột ngột.

###### 1.3.2.2 Trùng biến hình (Amoebae: Naked Amoebae & Testate Amoebae)
- **Trùng amip trần (Naked Amoebae, ví dụ *Amoeba proteus*):**
  - Di chuyển chậm chạp bằng chân giả (pseudopodia).
  - Phát triển mạnh khi hệ thống bị quá tải nghiêm trọng, oxy hòa tan suy kiệt kéo dài ($DO < 0.5\ \text{mg/L}$) hoặc bùn mới đưa vào nuôi cấy.
- **Trùng amip có vỏ (Testate Amoebae, ví dụ *Arcella*, *Euglypha*):**
  - Cơ thể được bảo vệ trong một lớp vỏ chitin hoặc silic.
  - Xuất hiện khi hệ thống có tải lượng hữu cơ ổn định nhưng dao động nhẹ, hoặc báo hiệu quá trình nitrat hóa bắt đầu hình thành.

##### 1.3.3 Động vật đa bào bậc cao: Luân trùng (Rotifers) và Tuyến trùng (Nematodes)

###### 1.3.3.1 Luân trùng (*Rotifera*: *Philodina*, *Brachionus*, *Habrotrocha*)
- **Đặc điểm cấu tạo:**
  - Động vật đa bào thực sự ($100 - 500\ \mu\text{m}$), cấu tạo cơ thể gồm đầu mang vành nhung mao quay như bánh xe (*corona*), thân và chân có hai ngón bám dính.
  - Có cơ quan nghiền thức ăn chuyên dụng (*mastax*) nghiền nát bông bùn và vi khuẩn.
- **Ý nghĩa chỉ thị vận hành:**
  - Báo hiệu hệ thống vận hành ở **tuổi bùn cao ($SRT > 15 - 20\ \text{ngày}$)**, tải lượng hữu cơ thấp ($F/M < 0.15\ \text{d}^{-1}$), môi trường cấp khí dồi dào ($DO > 2.5 - 3.0\ \text{mg/L}$).
  - Nước đầu ra có độ trong suốt cực cao, quá trình nitrat hóa diễn ra hoàn toàn ($NO_3^- - N$ cao, $NH_4^+ - N \approx 0$).
  - Tuy nhiên, nếu luân trùng phát sinh quá nhiều sẽ gây hiện tượng "tự ăn bùn", làm suy giảm nồng độ MLSS và tạo ra các mảnh vụn bông mịn.

###### 1.3.3.2 Tuyến trùng (*Nematodes*) và Giun nước (*Oligochaetes*: *Aeolosoma*)
- ***Nematodes* (Giun tròn):**
  - Cơ thể hình thoi dài ($0.5 - 2.0\ \text{mm}$), uốn lượn liên tục kiểu sóng hình sin.
  - Chuyên đào bới sâu vào lõi các bông bùn lớn để ăn cặn hữu cơ và vi khuẩn bên trong, tạo điều kiện cho oxy khuếch tán sâu vào trong tâm bông bùn.
  - Chỉ thị của **bùn quá già ($SRT > 25 - 40\ \text{ngày}$)**, hệ thống làm thoáng kéo dài (Extended Aeration), quá trình khoáng hóa nội sinh diễn ra mạnh mẽ.
- ***Aeolosoma* (Giun ít tơ):**
  - Giun đất hiển vi có các chấm đỏ/cam trên thân. Sự bùng nổ của *Aeolosoma* là bằng chứng của quá trình phân hủy bùn nội sinh triệt để, lượng bùn dư sinh ra rất thấp.

---

### 2. Động thái Lắng và Các Thông số Đánh giá Đặc tính Bông bùn (Flocculation & Sludge Settling Dynamics)

#### 2.1 Chỉ số Thể tích Bùn (Sludge Volume Index - SVI) và Phương pháp Thí nghiệm

##### 2.1.1 Định nghĩa toán học và Quy trình đo kiểm tiêu chuẩn (Standard Jar/Cylinder Settling Test)

###### 2.1.1.1 Công thức tính toán toán học của SVI
- **Định nghĩa chuẩn (Standard Methods 2710 D):**
  - Chỉ số thể tích bùn ($SVI$) là thể tích tính bằng mililít ($mL$) chiếm chỗ bởi $1\ \text{gam}$ bùn khô (chất rắn lơ lửng hỗn hợp bùn lỏng - $MLSS$) sau khi lắng tĩnh trong thời gian $30\ \text{phút}$ trong ống đong chuẩn dung tích $1000\ \text{mL}$.
- **Phương trình toán học:**
  $$SVI = \frac{SV_{30} \times 1000}{MLSS} \quad (\text{đơn vị: } \text{mL/g})$$
  - Hay biểu diễn dưới dạng mở rộng tương đương:
    $$SVI = \frac{SV_{30}\ (\text{mL/L}) \times 10^3\ (\text{mg/g})}{MLSS\ (\text{mg/L})} = \frac{SV_{30}\ (\text{mL/L})}{MLSS\ (\text{g/L})}$$
  - Trong đó:
    - $SV_{30}$: Thể tích lớp bùn lắng sau $30\ \text{phút}$ quan sát trên thang chia độ của ống đong ($mL/L$ hoặc $\%$ thể tích khi dùng ống $1000\ \text{mL}$).
    - $MLSS$: Nồng độ chất rắn lơ lửng của mẫu hỗn hợp bùn lỏng lấy từ bể hiếu khí ($mg/L$ hoặc $g/m^3$).
    - $1000$: Thừa số chuyển đổi đơn vị từ miligam ($mg$) sang gam ($g$).

###### 2.1.1.2 Biến thể chỉ số: SSVI (Stirred Specific Volume Index) và DSVI (Diluted SVI)
- **Hiện tượng cản trở thành bình (Wall Effect) ở ống đong tiêu chuẩn:**
  - Ống đong $1.0\ \text{L}$ thông thường ($d \approx 6\ \text{cm}$) có tỷ lệ diện tích thành bình trên thể tích lớn, sinh ra ma sát thành bình và dòng đối lưu cục bộ cản trở bông bùn lắng tự nhiên.
  - Khi $MLSS > 4000\ \text{mg/L}$, bùn đặc bị nén nghẽn (bridging), kết quả $SV_{30}$ phản ánh sai lệch khả năng lắng thực tế trong bể lắng đợt 2 quy mô lớn.
- **Chỉ số thể tích bùn có khuấy (Stirred Specific Volume Index - SSVI):**
  - Thực hiện trong cột lắng chuyên dụng đường kính $d \ge 10\ \text{cm}$, trang bị que khuấy chậm mảnh quay với vận tốc cực nhỏ ($1 - 2\ \text{rpm}$, vận tốc đầu cánh $\approx 1\ \text{cm/s}$) để phá vỡ hiện tượng bắc cầu cơ học và ma sát thành bình mà không làm vỡ bông cặn:
    $$SSVI = \frac{SV_{30, \text{stirred}} \times 1000}{MLSS} \quad (\text{mL/g})$$
  - Chuẩn hóa theo nồng độ $SSVI_{3.5}$ (nồng độ chuẩn $3.5\ \text{g/L} = 3500\ \text{mg/L}$) là thông số nền tảng dùng trong các thuật toán thiết kế bể lắng hiện đại (Metcalf & Eddy, WRC model).
- **Chỉ số thể tích bùn pha loãng (Diluted SVI - DSVI):**
  - Sử dụng cho bùn phình nặng ($SV_{30} > 800\ \text{mL/L}$).
  - Pha loãng hỗn hợp bùn lỏng bằng nước trong sau lắng theo cấp số nhân 2 ($1:1, 1:3, 1:7,\dots$) sao cho thể tích bùn sau 30 phút lắng $SV_{30}$ nằm trong khoảng $150 - 250\ \text{mL/L}$.
  - Tính toán:
    $$DSVI = \frac{SV_{30, \text{diluted}} \times 2^n \times 1000}{MLSS_{\text{original}}} \quad (\text{mL/g})$$
    ($n$ là số lần pha loãng nhân đôi).

##### 2.1.2 Thang phân loại khả năng lắng dựa trên SVI
- **$SVI < 70 - 80\ \text{mL/g}$ (Bùn già, lắng cực nhanh, dễ vỡ vụn):**
  - Bông bùn hình cầu nhỏ, đặc quánh, hàm lượng khoáng cao ($MLVSS/MLSS < 0.70$). Bùn rơi tự do rất nhanh nhưng để lại các hạt cặn lơ lửng mịn trong pha lỏng (Pin-point floc), nước đầu ra có độ đục cao.
- **$SVI = 80 - 150\ \text{mL/g}$ (Bùn lý tưởng, vận hành hoàn hảo):**
  - Cấu trúc "cốt thép - bê tông" cân đối, ranh giới giữa lớp bùn lắng và pha nước trong cực kỳ sắc nét, vận tốc lắng khối đạt $1.5 - 3.0\ \text{m/h}$. Nước sau lắng trong vắt, $TSS_e < 10\ \text{mg/L}$.
- **$SVI = 150 - 200\ \text{mL/g}$ (Bùn có xu hướng khó lắng - Ngưỡng cảnh báo):**
  - Bắt đầu phát triển quá mức vi khuẩn dạng sợi. Tốc độ hạ ranh giới bùn chậm chạp ($v_s \approx 0.8 - 1.2\ \text{m/h}$). Chiều dày lớp bùn đáy bể lắng tăng cao.
- **$SVI > 200 - 300\ \text{mL/g}$ (Phình bùn nghiêm trọng - Bulking Sludge):**
  - Bùn xốp như bọt biển, lắng không đáng kể sau 30 phút ($SV_{30} > 600 - 900\ \text{mL/L}$). Ranh giới bùn dâng cao chạm sát máng thu nước trong, nguy cơ tràn toàn bộ sinh khối ra nguồn tiếp nhận.

---

#### 2.2 Các Chế độ Lắng trong Bể lắng đợt 2 (Clarifier Settling Regimes)

##### 2.2.1 Bốn vùng lắng thủy lực theo phân loại Kynch & Fitch

###### 2.2.1.1 Lắng riêng rẽ (Discrete Settling - Type I) & Lắng keo tụ (Flocculent Settling - Type II)
- **Lắng riêng rẽ (Type I):**
  - Áp dụng cho các hạt rắn lơ lửng không tương tác, không thay đổi kích thước, hình dạng hay tỷ trọng trong suốt quá trình lắng (ví dụ hạt cát trong bể lắng cát).
  - Vận tốc lắng cân bằng giữa trọng lực, lực đẩy Archimedes và lực ma sát nhớt theo Định luật Stokes:
    $$v_s = \frac{g (\rho_p - \rho_w) d_p^2}{18 \mu}$$
    - $g$: Gia tốc trọng trường ($9.81\ \text{m/s}^2$)
    - $\rho_p, \rho_w$: Khối lượng riêng của hạt và của nước ($\text{kg/m}^3$)
    - $d_p$: Đường kính hạt ($\text{m}$)
    - $\mu$: Độ nhớt động lực học của nước ($\text{Pa}\cdot\text{s}$ hay $\text{N}\cdot\text{s/m}^2$)
- **Lắng keo tụ (Type II):**
  - Các hạt cặn hữu cơ trong quá trình lắng va chạm vào nhau, dính kết lại làm tăng kích thước và khối lượng riêng, dẫn đến vận tốc lắng tăng dần theo độ sâu bể lắng.

###### 2.2.1.2 Lắng cản trở / Lắng khối (Zone / Hindered Settling - Type III)
- **Đặc trưng cơ học:**
  - Xuất hiện ở nồng độ chất rắn trung bình đến cao ($MLSS > 1500 - 2000\ \text{mg/L}$).
  - Lực tương tác giữa các hạt liền kề rất lớn, giữ các bông bùn cố định vị trí tương đối với nhau. Toàn bộ khối chất rắn lắng xuống đồng thời như một tấm lưới hoặc một "piston", tạo ra một mặt phân cách chất lỏng - chất rắn (*sludge blanket interface*) rõ rệt giữa lớp bùn phía dưới và lớp nước trong phía trên.
- **Mô hình Vận tốc Lắng khối Vesilind:**
  - Vận tốc lắng khối $v_i$ phụ thuộc phi tuyến tính vào nồng độ chất rắn $X$:
    $$v_i = v_0 \cdot e^{-k_V \cdot X}$$
  - Trong đó:
    - $v_0$: Vận tốc lắng lý thuyết ở nồng độ chất rắn tiệm cận 0 ($m/h$, thường dao động $6.0 - 12.0\ \text{m/h}$).
    - $k_V$: Hệ số cản trở Vesilind ($m^3/\text{kg}$ hoặc $L/\text{g}$, thường dao động $0.3 - 0.6\ \text{m}^3/\text{kg}$). Hệ số $k_V$ tương quan thuận chặt chẽ với chỉ số $SVI$: Bùn có $SVI$ càng cao thì $k_V$ càng lớn, làm vận tốc lắng $v_i$ sụt giảm cực nhanh khi tăng nồng độ.

###### 2.2.1.3 Lắng nén (Compression Settling - Type IV)
- **Đặc trưng cơ học:**
  - Xảy ra ở đáy bể lắng đợt 2 nơi nồng độ bùn đạt giá trị đậm đặc nhất ($X > 6000 - 12000\ \text{mg/L}$).
  - Các bông bùn tựa trực tiếp lên nhau tạo thành cấu trúc khung liên tục chịu lực. Quá trình lắng tiếp theo chỉ có thể diễn ra khi khối lượng của các lớp bùn mới lắng phía trên đè ép cơ học xuống, thắng được lực kháng cấu trúc và ép lượng nước nằm trong các lỗ rỗng kẽ hạt thoát ngược lên trên.

##### 2.2.2 Tải trọng chất rắn bề mặt (Solids Loading Rate - SLR) và Tải trọng thủy lực bề mặt (Surface Overflow Rate - SOR)

###### 2.2.2.1 Tải trọng chất rắn bề mặt (Solids Loading Rate - SLR)
- **Khái niệm và Công thức tính toán:**
  - $SLR$ biểu thị tổng khối lượng chất rắn đưa vào một đơn vị diện tích mặt thoáng bể lắng đợt 2 trong một đơn vị thời gian:
    $$SLR = \frac{(Q + Q_R) \times MLSS}{A_{\text{clarifier}}} \quad (\text{đơn vị: } \text{kg } TSS/m^2\cdot d \text{ hoặc } \text{kg } TSS/m^2\cdot h)$$
  - Trong đó:
    - $Q$: Lưu lượng nước thải đầu vào trạm ($m^3/d$ hoặc $m^3/h$)
    - $Q_R$: Lưu lượng bùn hoạt tính tuần hoàn trở lại bể hiếu khí ($RAS$, $m^3/d$ hoặc $m^3/h$)
    - $MLSS$: Nồng độ chất rắn lơ lửng hỗn hợp bùn lỏng ($g/m^3$ hoặc $mg/L$, lưu ý $1\ g/m^3 = 10^{-3}\ \text{kg/m}^3$)
    - $A_{\text{clarifier}}$: Tổng diện tích bề mặt hữu ích của bể lắng đợt 2 ($m^2$)
- **Tiêu chuẩn thiết kế kỹ thuật (Metcalf & Eddy / EPA standards):**
  - Lưu lượng trung bình ($Average\ flow$): $SLR = 4.0 - 6.0\ \text{kg } TSS/m^2\cdot h$ ($100 - 150\ \text{kg/m}^2\cdot d$).
  - Lưu lượng cực đại ($Peak\ flow$): $SLR_{\text{peak}} \le 8.0 - 10.0\ \text{kg } TSS/m^2\cdot h$ ($200 - 240\ \text{kg/m}^2\cdot d$).
  - Nếu $SLR$ vượt quá tải trọng lắng giới hạn ($Limiting\ Solids\ Flux\ - G_L$), đáy bể lắng sẽ tích lũy chất rắn liên tục, mặt lớp bùn dâng cao gây tràn bùn nghiêm trọng.

###### 2.2.2.2 Tải trọng thủy lực bề mặt (Surface Overflow Rate - SOR)
- **Công thức tính toán:**
  $$SOR = \frac{Q}{A_{\text{clarifier}}} \quad (\text{đơn vị: } m^3/m^2\cdot d \text{ hoặc } m/h)$$
  *(Lưu ý: Tính toán SOR chỉ dựa trên lưu lượng nước thải $Q$, không cộng thêm lưu lượng tuần hoàn $Q_R$ vì $Q_R$ được rút ra ở đáy bể).*
- **Tiêu chuẩn thiết kế kỹ thuật:**
  - Cho bùn hoạt tính thông thường: $SOR_{\text{avg}} = 16 - 28\ m^3/m^2\cdot d$ ($0.7 - 1.2\ m/h$); $SOR_{\text{peak}} \le 40 - 48\ m^3/m^2\cdot d$ ($1.6 - 2.0\ m/h$).
  - Cho bùn hoạt tính làm thoáng kéo dài: $SOR_{\text{avg}} = 8 - 16\ m^3/m^2\cdot d$ ($0.3 - 0.7\ m/h$).
- **Tải trọng máng thu nước (Weir Overflow Rate - WOR):**
  $$WOR = \frac{Q}{L_{\text{weir}}} \quad (\text{đơn vị: } m^3/m\cdot d)$$
  - Giới hạn thiết kế: $WOR \le 125 - 250\ m^3/m\cdot d$ để tránh tạo phễu hút thủy lực kéo cặn lắng qua máng răng cưa V-notch.

---

### 3. Hiện tượng Bất thường Vận hành: Nguyên nhân, Động thái và Giải pháp Khắc phục (Operational Anomalies, Root Causes & Control Strategies)

#### 3.1 Phình bùn (Sludge Bulking)

##### 3.1.1 Phân loại phình bùn

###### 3.1.1.1 Phình bùn do vi khuẩn dạng sợi (Filamentous Bulking)
- Chiếm $> 90\%$ các trường hợp sự cố lắng tại các trạm xử lý nước thải sinh hoạt và công nghiệp.
- Mạng lưới sợi vi khuẩn vươn dài tự do ra khỏi cấu trúc bông bùn, ngăn cản cơ chế ép nước và nén chặt của các bông bùn ở vùng lắng cản trở và lắng nén.
- Thể tích bùn lắng $SV_{30} > 600 - 900\ \text{mL/L}$, $SVI > 150 - 400\ \text{mL/g}$, nhưng nước trong tách pha phía trên vẫn có thể rất trong nếu không bị cuốn trôi.

###### 3.1.1.2 Phình bùn không do dạng sợi (Non-filamentous / Zoogloeal / Viscous Bulking)
- Xuất hiện khi vi khuẩn tạo bông (*Zoogloea* spp.) bị kích thích sản sinh quá mức các polyme ngoại bào nhớt dạng nhầy ngậm nước (*slime/gel matrix*).
- Nguyên nhân: Nước thải chứa hàm lượng đường hòa tan hoặc acid hữu cơ cực cao nhưng thiếu hụt trầm trọng dưỡng chất Nitơ hoặc Phospho ($BOD : N : P \approx 100 : 1 : 0.2$), hoặc do tải lượng hữu cơ đột biến ($F/M > 1.0\ \text{d}^{-1}$).
- Đặc điểm nhận diện: Soi kính hiển vi không thấy sợi vi khuẩn; hỗn hợp bùn có độ nhớt cực cao, sủi bọt nhớt dính; nước sau lắng nhớt và cản trở truyền oxy; khử nước trên máy ép bùn cực kỳ khó khăn.

##### 3.1.2 Nguyên nhân gốc rễ (Root Causes) và Sinh thái học vi sinh

###### 3.1.2.1 Thiếu hụt Oxy hòa tan ($DO < 1.0 - 1.5\ \text{mg/L}$)
- **Cơ chế cạnh tranh động học:**
  - Tỷ số diện tích tiếp xúc trên thể tích tế bào ($A/V$) của vi khuẩn dạng sợi (hình trụ dài mảnh) cao gấp $5 - 10$ lần so với vi khuẩn tạo bông dạng khối cầu.
  - Hằng số bão hòa oxy của vi khuẩn sợi rất nhỏ ($K_{O2} \approx 0.05 - 0.1\ \text{mg/L}$), trong khi vi khuẩn tạo bông nằm sâu trong khối matrix EPS có $K_{O2} \approx 0.2 - 0.5\ \text{mg/L}$.
  - Khi nồng độ DO trong bể hiếu khí tụt xuống $< 1.0\ \text{mg/L}$, tốc độ sinh trưởng của vi khuẩn tạo bông bị suy giảm nghiêm trọng theo phương trình Monod:
    $$\mu = \mu_{\max} \left(\frac{DO}{K_{O2} + DO}\right)$$
    Vi khuẩn sợi hấp thụ oxy dễ dàng hơn, vươn sợi ra ngoài để đón oxy và chiếm ưu thế sinh khối tuyệt đối (*Sphaerotilus natans*, Type 1701, *Haliscomenobacter hydrossis*).

###### 3.1.2.2 Tải lượng hữu cơ thấp kéo dài ($F/M < 0.10\ \text{kg } BOD_5/\text{kg } MLVSS\cdot d$)
- **Động học chọn lọc Oligotrophic:**
  - Khi cơ chất hòa tan trong bể luôn ở mức tiệm cận cạn kiệt (đặc trưng của bể làm thoáng kéo dài hoặc bể CMAS thiết kế dư dung tích), các loài vi khuẩn sợi có ái lực cơ chất cực cao (hằng số Monod $K_s$ cực thấp $\approx 0.5 - 2\ \text{mg/L}$) như *Microthrix parvicella*, Type 0041, Type 0675 sẽ cạnh tranh dinh dưỡng hiệu quả hơn vi khuẩn tạo bông ($K_s \approx 10 - 20\ \text{mg/L}$).

###### 3.1.2.3 Thiếu hụt Dinh dưỡng Đa lượng (Nitrogen & Phosphorus Deficiency)
- Tỷ lệ dinh dưỡng tối ưu cho quá trình hiếu khí:
  $$BOD_5 : N : P = 100 : 5 : 1 \quad \text{hoặc} \quad COD : N : P = 100 : 2.5 : 0.5$$
- Khi tỷ lệ $N$ hoặc $P$ sụt giảm, vi khuẩn tạo bông không thể tổng hợp protein cấu trúc tế bào và enzyme, trong khi các loài vi khuẩn sợi chuyên biệt (*Thiothrix*, Type 021N) có khả năng sinh tổng hợp enzyme phosphatase ngoại bào mạnh mẽ và tích lũy phosphate/sulfur dự trữ nội bào để sinh sôi.

###### 3.1.2.4 Nước thải lưu cữu thối rữa (Septic Wastewater & High Sulfide)
- Thời gian lưu nước trong mạng lưới cống dài, nhiệt độ cao sinh ra điều kiện kỵ khí trong đường ống, vi khuẩn khử sulfate chuyển hóa $SO_4^{2-}$ thành $H_2S$ hòa tan và các acid béo bay hơi ($VFAs$).
- Nước thải đầu vào giàu sulfide ($S^{2-} > 2 - 5\ \text{mg/L}$) tạo môi trường kích thích bùng nổ các loài vi khuẩn oxy hóa lưu huỳnh dạng sợi (*Thiothrix nivea*, *Beggiatoa*, Type 021N).

###### 3.1.2.5 Thủy lực hoàn toàn xáo trộn (Complete-Mix Reactor vs Plug-Flow)
- Bể CMAS phân tán đều nồng độ cơ chất ngay tại điểm vào, duy trì nồng độ chất hữu cơ thấp đồng nhất trên toàn bộ thể tích bể $\rightarrow$ triệt tiêu gradient nồng độ, tước đoạt lợi thế động học của vi khuẩn tạo bông và tạo điều kiện lý tưởng cho vi khuẩn sợi phát triển.

##### 3.1.3 Các giải pháp kỹ thuật kiểm soát và ngăn chặn phình bùn (Remediation & Control)

###### 3.1.3.1 Bể phản ứng chọn lọc (Biological Selectors): Nguyên lý Động học Cạnh tranh
- **Cơ chế Feasting - Fasting (No - Đói):**
  - Thiết kế một hoặc nhiều ngăn phản ứng thể tích nhỏ đặt ngay trước bể aerotank chính, tiếp nhận toàn bộ dòng nước thải đầu vào ($Q$) và dòng bùn tuần hoàn ($Q_R$).
  - Tạo ra gradient nồng độ cơ chất hòa tan cực lớn tại vùng đầu dòng (*Feast zone*).
  - Vi khuẩn tạo bông có vận tốc hấp thu cơ chất cực đại ($k_{\max}$) và vận tốc sinh trưởng cực đại ($\mu_{\max}$) lớn gấp nhiều lần vi khuẩn sợi. Trong vùng "No cơ chất", vi khuẩn tạo bông hấp thụ thần tốc cơ chất hòa tan và lưu trữ dưới dạng glycogen hoặc PHB nội bào. Khi hỗn hợp chuyển sang vùng "Đói cơ chất" (bể chính), vi khuẩn tạo bông tiêu thụ lượng cơ chất dự trữ này để sinh trưởng, trong khi vi khuẩn sợi bị bỏ đói hoàn toàn.
- **Phân loại Bể chọn lọc:**
  - *Aerobic Selector* (Bể chọn lọc hiếu khí):
    - Thể tích tương ứng thời gian lưu thủy lực ngắn: $HRT = 15 - 30\ \text{phút}$.
    - Sục khí cưỡng bức duy trì nồng độ $DO > 2.0 - 3.0\ \text{mg/L}$.
    - Tải lượng $F/M$ cục bộ rất cao: $F/M_{\text{selector}} = 1.5 - 3.0\ \text{kg } BOD_5/\text{kg } MLVSS\cdot d$.
  - *Anoxic Selector* (Bể chọn lọc thiếu khí):
    - Không cấp oxy hòa tan ($DO < 0.2\ \text{mg/L}$), tiếp nhận dòng nitrate ($NO_3^-$) từ nước nội tuần hoàn hoặc dòng bùn $RAS$.
    - Vi khuẩn dị dưỡng tạo bông có khả năng khử nitrate (*denitrifiers*) sử dụng $NO_3^-$ làm chất nhận electron để oxy hóa cơ chất, trong khi đa số vi khuẩn sợi là hiếu khí bắt buộc không thể sử dụng nitrate, do đó bị ức chế.
  - *Anaerobic Selector* (Bể chọn lọc kỵ khí):
    - Hoàn toàn không có cả $O_2$ và $NO_3^-$.
    - Kích thích chọn lọc vi khuẩn tích lũy photpho (*PAOs*) hấp thu acid béo bay hơi ($VFAs$) và tích lũy polyhydroxyalkanoates ($PHA$), loại bỏ hoàn toàn các vi khuẩn sợi thông thường (*S. natans*, Type 1701).

###### 3.1.3.2 Biện pháp khẩn cấp: Khử trùng chọn lọc bằng Hóa chất (Chlorination / $H_2O_2$ dosing)
- **Vị trí và Điểm châm Clo tối ưu:**
  - Không châm trực tiếp vào bể aerotank vì thể tích lớn và gây chết vi sinh vật diện rộng.
  - **Châm vào dòng bùn hoạt tính tuần hoàn ($RAS$):** Nơi nồng độ bùn đậm đặc, lưu lượng ổn định, thể tích đường ống nhỏ đảm bảo thời gian tiếp xúc ngắn ($t_c = 2 - 5\ \text{phút}$) và tần suất bùn đi qua điểm châm cao ($2 - 3\ \text{lần/ngày}$).
- **Liều lượng tính toán và Kiểm soát:**
  - Liều lượng Clo hữu hiệu:
    $$\text{Dose}_{\text{target}} = 2.0 - 6.0\ \text{kg } Cl_2 / 1000\ \text{kg } MLSS_{\text{system}}\cdot d$$
    (Thông thường bắt đầu ở mức thấp $2.0 - 3.0\ \text{kg } Cl_2/1000\ \text{kg } MLSS\cdot d$, tăng dần nếu SVI chưa hạ).
  - Nồng độ Clo duy trì trong đường ống RAS: $C_{\text{pipe}} = 10 - 20\ \text{mg/L}$.
- **Cơ chế bảo vệ sinh học:**
  - Các sợi vi khuẩn vươn dài ra ngoài pha lỏng có diện tích tiếp xúc trực tiếp lớn sẽ bị Clo oxy hóa phá hủy màng tế bào trước tiên.
  - Vi khuẩn tạo bông nằm sâu bên trong cấu trúc gel EPS được che chở, chỉ có lớp vi khuẩn ngoài rìa bị tổn thương nhẹ.
  - Dấu hiệu ngưng châm Clo: SVI giảm xuống dưới $150\ \text{mL/g}$, quan sát kính hiển vi thấy các sợi vi khuẩn bị đứt gãy, biến dạng, tế bào sợi bị rỗng ruột (*empty sheaths*), độ đục nước sau lắng tăng nhẹ.

---

#### 3.2 Hiện tượng Bọt sinh học (Sludge Foaming & Scum Formation)

##### 3.2.1 Vi sinh vật gây bọt: *Nocardioforms* (*Gordonia amarae*) và *Microthrix parvicella*

###### 3.2.1.1 Cấu tạo vách tế bào kỵ nước và Acid Mycolic
- Vi sinh vật họ *Nocardioforms* (chủ yếu là xạ khuẩn *Gordonia amarae*, *Nocardia asteroides*, *Skermania piniformis*) là vi khuẩn Gram dương phân nhánh thực sự.
- Vách tế bào chứa hàm lượng cực cao các acid béo mạch nhánh hydroxyl hóa gọi là **Acid Mycolic** ($C_{30} - C_{90}$):
  - Mang lại tính kỵ nước (hydrophobicity) cực mạnh cho bề mặt tế bào.
  - Bề mặt tế bào có góc tiếp xúc với nước lớn ($\theta_c > 70 - 90^\circ$).

###### 3.2.1.2 Cơ chế tạo bọt 3 pha (Gas - Liquid - Solid Three-Phase Emulsion)
- Khi bọt khí sục vào từ đáy bể hiếu khí, các tế bào vi khuẩn kỵ nước có xu hướng né tránh pha nước, bám dính chặt chẽ vào bề mặt tiếp xúc liên pha giữa bọt khí và nước.
- Bọt khí đóng vai trò như hạt tuyển nổi, mang vi khuẩn kỵ nước cùng với các hạt chất béo, dầu mỡ không tan ($FOG$) nổi lên bề mặt chất lỏng.
- Tại mặt thoáng, lớp màng sinh học kỵ nước bao bọc lấy bọt khí, ngăn cản bọt khí vỡ ra, hình thành lớp bọt nhớt dày từ $10 - 50\ \text{cm}$, màu nâu sẫm (chocolate brown), dai, không tan dưới tác động của vòi phun nước thông thường.

##### 3.2.2 Biện pháp kiểm soát bọt

###### 3.2.2.1 Xả bùn chọn lọc bề mặt (Surface Waste Activated Sludge - Surface WAS)
- **Nghịch lý tuổi bùn của Nocardia:**
  - Bọt vi khuẩn nổi trên bề mặt không đi qua cửa thu đáy để sang bể lắng, do đó không bị thải bỏ qua hệ thống xả bùn đáy ($WAS$) thông thường.
  - Tuổi bùn thực tế của quần thể *Nocardia* trên mặt bể có thể lên tới $50 - 100\ \text{ngày}$, dù trạm vận hành ở $SRT = 5\ \text{ngày}$.
- **Giải pháp:** Thiết kế máng gạt thu váng bọt bề mặt (scum skimmer) chuyên dụng trên mặt bể aerotank và bể lắng để bơm xả trực tiếp lớp bọt sang khu xử lý bùn (*selective surface wasting*).

###### 3.2.2.2 Kiểm soát Dầu mỡ (FOG) đầu vào và Phun hóa chất
- Vận hành tối ưu bể tuyển nổi DAF hoặc bể lắng đợt 1 để loại bỏ triệt để FOG ($FOG < 25 - 50\ \text{mg/L}$ vào bể sinh học).
- Phun dung dịch Clo loãng ($50 - 100\ \text{mg/L}$) hoặc chất phá bọt chuyên dụng trực tiếp lên bề mặt lớp bọt để oxy hóa lớp màng ngoài của xạ khuẩn.
- Hạ tuổi bùn của trạm xuống $SRT < 5\ \text{ngày}$ (ở nhiệt độ $> 20^\circ\text{C}$) để tốc độ sinh trưởng của vi khuẩn tạo bông vượt qua tốc độ nhân đôi chậm chạp của xạ khuẩn *Nocardioforms*.

---

#### 3.3 Hiện tượng Bùn nổi do Khử Nitrat trong Bể lắng (Rising Sludge / Clarifier Denitrification)

##### 3.3.1 Cơ chế sinh hóa và Động thái tuyển nổi

###### 3.3.1.1 Phản ứng khử nitrat kỵ khí cục bộ trong lớp bùn lắng đáy
- Khi bể hiếu khí thực hiện quá trình nitrat hóa tốt, nước lỏng đưa sang bể lắng đợt 2 chứa nồng độ Nitrate cao ($NO_3^- - N = 15 - 30\ \text{mg/L}$).
- Tại đáy bể lắng đợt 2, bùn hoạt tính tập trung dày đặc, lượng oxy hòa tan hòa lẫn nhanh chóng bị cạn kiệt ($DO \rightarrow 0$).
- Môi trường chuyển sang trạng thái thiếu khí (anoxic). Các vi khuẩn dị dưỡng tùy nghi sử dụng nitrate làm chất nhận electron cuối cùng, dị hóa các chất hữu cơ nội bào để thực hiện phản ứng khử nitrat:
  $$2\text{NO}_3^- + 10e^- + 12\text{H}^+ \rightarrow \text{N}_2 \uparrow + 6\text{H}_2\text{O}$$

###### 3.3.1.2 Hiện tượng túi khí $N_2$ bám vào bông bùn
- Khí nitơ ($N_2$) sinh ra có độ hòa tan trong nước rất thấp ($H \approx 0.015\ \text{g/kg}$ ở $20^\circ\text{C}$), nhanh chóng đạt trạng thái quá bão hòa và hình thành hàng triệu bọt khí vi mô ($d < 50\ \mu\text{m}$).
- Các bọt khí $N_2$ bị giữ lại và mắc kẹt trong mạng lưới xốp của bông bùn đáy bể.
- Khối lượng riêng biểu kiến trung bình của cụm "bông bùn + bọt khí" ($\rho_{\text{apparent}}$) tụt xuống thấp hơn khối lượng riêng của nước:
  $$\rho_{\text{apparent}} = \frac{m_{\text{floc}} + m_{\text{gas}}}{V_{\text{floc}} + V_{\text{gas}}} < \rho_{\text{water}} \approx 1000\ \text{kg/m}^3$$
- Lực đẩy nổi vượt qua trọng lực, làm các tảng bùn lớn tách đáy, nổi phềnh lên bề mặt bể lắng đợt 2 (*clumping / rising sludge*).

##### 3.3.2 Phân biệt Bùn nổi (Rising Sludge) và Phình bùn (Bulking Sludge)

| Tiêu chí So sánh | Hiện tượng Bùn nổi (Rising Sludge) | Hiện tượng Phình bùn (Bulking Sludge) |
| :--- | :--- | :--- |
| **Đặc tính lắng trong ống đong (SVI test)** | Bùn lắng cực tốt trong $10 - 20\ \text{phút}$ đầu ($SV$ giảm sâu), sau đó các mảng bùn tự nổi ngược lên mặt sau $30 - 60\ \text{phút}$. | Bùn từ chối lắng ngay từ phút đầu tiên, ranh giới hạ cực chậm, thể tích bùn sau 30 phút rất lớn ($SV_{30} > 600\ \text{mL}$). |
| **Chỉ số SVI** | Thấp đến trung bình ($SVI < 100 - 120\ \text{mL/g}$). | Rất cao ($SVI > 150 - 300\ \text{mL/g}$). |
| **Hình thái trên mặt bể lắng** | Từng mảng bùn lớn màu nâu sẫm nổi lên, bề mặt mảng bùn có bọt khí sủi tăm li ti vỡ ra. | Toàn bộ bề mặt bể lắng bao phủ bởi lớp bùn đồng nhất dâng sát máng thu, không có mảng tách biệt. |
| **Chất lượng nước trong xen kẽ** | Rất trong, độ đục cực thấp giữa các mảng bùn nổi. | Nước đục nhẹ hoặc mờ ảo do vi khuẩn sợi vươn ra. |
| **Nguyên nhân cốt lõi** | Khử nitrate yếm khí sinh khí $N_2$ tuyển nổi. | Vi khuẩn sợi phát triển quá mức cản trở nén cơ học. |

##### 3.3.3 Biện pháp kiểm soát Bùn nổi
- Tăng tỷ lệ tuần hoàn bùn ($Q_R$): Giảm thiểu thời gian lưu của bùn tại đáy bể lắng xuống dưới $1.0 - 1.5\ \text{giờ}$.
- Cải tạo hoặc lắp đặt ngăn thiếu khí (Anoxic Tank) phía trước aerotank: Thực hiện khử nitrat có chủ đích bằng cơ chất hữu cơ tươi của nước thải, giảm nồng độ $NO_3^-$ vào bể lắng xuống $< 5 - 8\ \text{mg/L}$.
- Cải tiến hệ thống cào bùn: Thay thế gạt bùn kiểu xoay chậm bằng hệ thống hút bùn thủy tĩnh kiểu ống thu phân đoạn (*suction-header sludge collector*) để rút bùn ra ngay lập tức khi vừa chạm đáy.

---

#### 3.4 Bông cặn mịn / Bông cặn kim (Pin-Point Floc) và Bùn phân tán (Dispersed Growth)

##### 3.4.1 Pin-Point Floc (Bông bùn cặn kim)
- **Đặc trưng:**
  - Bông bùn có kích thước rất nhỏ ($20 - 50\ \mu\text{m}$), dạng hạt tròn cô đặc, thiếu hoàn toàn các sợi vi khuẩn làm khung giằng bên ngoài.
  - Lắng rất nhanh trong bài đo $SVI$ ($SVI < 60 - 80\ \text{mL/g}$), đáy ống đong nén chặt, nhưng phần nước trong bên trên mờ đục chứa đầy các chấm bông cặn kim li ti không lắng được.
- **Nguyên nhân:**
  - Vận hành ở tuổi bùn quá dài ($SRT > 25 - 40\ \text{ngày}$) và tải lượng $F/M$ cực thấp.
  - Quá trình phân hủy nội sinh kéo dài làm cạn kiệt năng lượng tế bào, EPS bị vi khuẩn tự tiêu thụ làm suy yếu lực dính, kết hợp với lực cắt thủy lực mạnh của cánh khuấy hoặc bọt khí xé rách bông bùn.
- **Giải pháp:** Tăng lưu lượng xả bùn ($WAS$) để hạ tuổi bùn xuống dải tối ưu ($5 - 12\ \text{ngày}$), giảm bớt cường độ sục khí nếu DO đang dư thừa quá mức ($DO > 4 - 5\ \text{mg/L}$).

##### 3.4.2 Dispersed Growth (Bùn sinh trưởng phân tán)
- **Đặc trưng:**
  - Vi khuẩn không kết dính thành bông, tồn tại ở dạng đơn bào tự do lơ lửng trong nước.
  - Nước sau lắng đục ngầu như sữa, giá trị đục và $TSS_e$ cực cao ($> 100\ \text{mg/L}$), hiệu quả lắng trọng lực gần như bằng không.
- **Nguyên nhân:**
  - Sốc tải hữu cơ cực mạnh làm vi khuẩn rơi vào pha tăng trưởng logarit không kiểm soát.
  - Nước thải đầu vào có độc chất ức chế sinh học (axit, kiềm mạnh làm $\text{pH} < 6.0$ hoặc $> 9.0$, kim loại nặng $\text{Cu, Cr, Ni, Zn}$, chất hoạt động bề mặt cao, chất tẩy clo).
- **Giải pháp:** Trung hòa pH khẩn cấp; bổ sung chất trợ lắng keo tụ phèn nhôm ($\text{Al}^{3+}$), phèn sắt ($\text{Fe}^{3+}$) hoặc polymer cation để tạo bông cưỡng bức; dẫn nước thải ô nhiễm độc chất vào bể điều hòa để pha loãng.

---

### 4. Các Thông số Vận hành Cơ bản và Cân bằng Vật chất (Fundamental Operational Parameters & Process Balances)

#### 4.1 Tỷ số Thức ăn trên Vi sinh vật (Food-to-Microorganism Ratio - F/M)

##### 4.1.1 Định nghĩa toán học và Bản chất vật lý
- **Ý nghĩa kỹ thuật:**
  - Tỷ số $F/M$ định lượng tải trọng hữu cơ đưa vào hệ thống tính trên một đơn vị khối lượng vi sinh vật hoạt tính trong một ngày đêm.
  - Là đại lượng quyết định trực tiếp đến trạng thái sinh trưởng của vi khuẩn (tăng trưởng logarit, tăng trưởng suy giảm hay phân hủy nội sinh), từ đó quyết định tính tạo bông và hiệu suất xử lý.
- **Biểu thức toán học tiêu chuẩn:**
  $$F/M = \frac{Q \cdot S_0}{V \cdot X} \quad (\text{đơn vị: } \text{kg } BOD_5 / \text{kg } MLVSS\cdot d \text{ hoặc } d^{-1})$$
  - Có thể biểu diễn qua thời gian lưu thủy lực $\theta$:
    $$F/M = \frac{S_0}{\theta \cdot X}$$
- **Quy đổi biến số và Thứ nguyên đồng nhất:**
  - $Q$: Lưu lượng nước thải dòng vào bể sinh học ($m^3/d$)
  - $S_0$: Nồng độ cơ chất hữu cơ đầu vào bể hiếu khí, tính theo $BOD_5$ hoặc $COD$ hòa tan phân hủy sinh học ($g/m^3 \equiv mg/L \equiv g/m^3$)
  - $V$: Thể tích hữu ích của bể phản ứng hiếu khí ($m^3$)
  - $X$: Nồng độ sinh khối vi sinh vật trong bể, biểu thị qua chất rắn lơ lửng bay hơi ($MLVSS$, $g/m^3 \equiv mg/L$). Nếu tính theo tổng chất rắn ($MLSS$), phải ghi chú rõ là $F/M_{\text{MLSS}}$.
  - $\theta = V/Q$: Thời gian lưu nước thủy lực ($HRT$, ngày $d$)

##### 4.1.2 Dải giá trị thiết kế và vận hành đặc trưng
- **Bùn hoạt tính truyền thống hoàn toàn xáo trộn (CMAS):**
  $$F/M = 0.20 - 0.60\ \text{kg } BOD_5 / \text{kg } MLVSS\cdot d$$
- **Bùn hoạt tính làm thoáng kéo dài (Extended Aeration / Bể Oxy mương oxy hóa):**
  $$F/M = 0.05 - 0.15\ \text{kg } BOD_5 / \text{kg } MLVSS\cdot d$$
- **Bùn hoạt tính cao tải (High-Rate Activated Sludge):**
  $$F/M = 0.60 - 1.50\ \text{kg } BOD_5 / \text{kg } MLVSS\cdot d$$
- **Bể lọc sinh học màng (MBR):**
  $$F/M = 0.08 - 0.20\ \text{kg } BOD_5 / \text{kg } MLVSS\cdot d$$

---

#### 4.2 Thời gian Lưu bùn / Tuổi bùn (Solids Retention Time - SRT / Mean Cell Residence Time - MCRT)

##### 4.2.1 Cân bằng chất rắn toàn hệ thống và Thiết lập công thức

###### 4.2.1.1 Phương trình cân bằng vật chất chất rắn sinh học ở trạng thái dừng
- Thiết lập ranh giới hệ thống bao gồm: Bể phản ứng hiếu khí ($Aerotank$) và Bể lắng đợt 2 ($Secondary\ Clarifier$).
- Phương trình bảo toàn khối lượng sinh khối:
  $$\text{Tích lũy} = \text{Vào} - \text{Ra} + \text{Sinh trưởng ròng}$$
  Ở trạng thái dừng ($\text{Steady State}$), tích lũy $= 0$, giả định nồng độ sinh khối đầu vào bằng 0 ($X_0 \approx 0$):
  $$\text{Sinh trưởng ròng} = \text{Khối lượng sinh khối xả ra ngoài hệ thống mỗi ngày}$$
- Khái niệm Tuổi bùn ($\theta_c$ hay $SRT$):
  $$\theta_c = SRT = \frac{\text{Tổng khối lượng sinh khối có trong hệ thống (kg)}}{\text{Tổng khối lượng sinh khối bị loại bỏ khỏi hệ thống mỗi ngày (kg/d)}}$$

###### 4.2.1.2 Biểu thức toán học chi tiết
- **Trường hợp tổng quát (Bùn xả từ đáy bể lắng và có cặn trôi qua máng thu nước trong):**
  $$SRT = \theta_c = \frac{V \cdot X}{(Q - Q_w) X_e + Q_w X_w} \approx \frac{V \cdot X}{Q_e X_e + Q_w X_R}$$
  - Trong đó:
    - $V$: Thể tích bể hiếu khí ($m^3$)
    - $X$: Nồng độ bùn trong bể hiếu khí ($MLVSS$ hoặc $MLSS$, $mg/L$)
    - $Q$: Lưu lượng nước thải đầu vào trạm ($m^3/d$)
    - $Q_w$: Lưu lượng bùn xả dư mỗi ngày từ dòng đáy bể lắng ($m^3/d$)
    - $X_w \equiv X_R$: Nồng độ bùn trong dòng xả đáy / bùn tuần hoàn ($mg/L$)
    - $Q_e = Q - Q_w$: Lưu lượng nước trong xả ra sau lắng đợt 2 ($m^3/d$)
    - $X_e$: Nồng độ chất rắn lơ lửng còn sót lại trôi theo nước sau lắng ($mg/L$)
- **Trường hợp xả bùn trực tiếp từ bể phản ứng hiếu khí (Hydraulic Waste Method):**
  - Vì xả trực tiếp từ bể aerotank nên nồng độ bùn xả chính bằng nồng độ trong bể ($X_w = X$). Bỏ qua cặn trôi ra máng ($X_e \approx 0$):
    $$SRT = \frac{V \cdot X}{Q_w \cdot X} = \frac{V}{Q_w}$$
  - Phương pháp này cực kỳ đơn giản trong vận hành thực tế: Để duy trì $SRT = 10\ \text{ngày}$, mỗi ngày chỉ cần xả bỏ đúng $\frac{1}{10}$ thể tích bể hiếu khí ($Q_w = V / 10$).

##### 4.2.2 Mối liên hệ cốt lõi giữa SRT và F/M qua Động học Vi sinh Monod
- Từ cân bằng cơ chất và sinh khối:
  $$\frac{1}{SRT} = Y \cdot U - b$$
  - Với $U$ là tốc độ sử dụng cơ chất riêng ($Specific\ substrate\ utilization\ rate$):
    $$U = \frac{Q(S_0 - S)}{V \cdot X} = (F/M) \times E_{\text{removal}}$$
  - $E_{\text{removal}} = \frac{S_0 - S}{S_0}$ là hiệu suất khử cơ chất.
- Khi hiệu suất xử lý cao ($E_{\text{removal}} \approx 1.0$, tức $S \ll S_0$):
  $$\frac{1}{SRT} \approx Y \cdot (F/M) - b$$
  - $Y$: Hệ số sản lượng sinh khối lý thuyết ($g\ VSS/g\ BOD_5$ hoặc $g\ VSS/g\ COD$)
  - $b$: Hệ số phân hủy nội sinh của vi sinh vật ($d^{-1}$)
- **Ý nghĩa kỹ thuật sâu sắc:** $SRT$ và $F/M$ là hai mặt của một đồng xu. Vận hành ở $SRT$ dài bắt buộc kéo theo $F/M$ thấp (vi khuẩn già, tự oxy hóa nội sinh cao), ngược lại $SRT$ ngắn tương ứng với $F/M$ cao (vi khuẩn trẻ, sinh trưởng nhanh).

---

#### 4.3 Thời gian Lưu nước Thủy lực (HRT) và Tải trọng Hữu cơ Thể tích (OLR)

##### 4.3.1 Thời gian lưu nước thủy lực (Hydraulic Retention Time - HRT)
- **Công thức tính toán:**
  $$\theta = HRT = \frac{V}{Q} \quad (\text{đơn vị: } \text{ngày } d \text{ hoặc giờ } h = \frac{V \times 24}{Q})$$
- Dải giá trị thiết kế:
  - CMAS thông thường: $HRT = 4.0 - 8.0\ \text{h}$
  - Làm thoáng kéo dài: $HRT = 18.0 - 36.0\ \text{h}$
  - MBR: $HRT = 3.0 - 6.0\ \text{h}$

##### 4.3.2 Tải trọng hữu cơ thể tích (Volumetric Organic Loading Rate - OLR / $L_{\text{org}}$)
- **Công thức tính toán:**
  $$OLR = \frac{Q \cdot S_0}{V} = \frac{S_0}{HRT} \quad (\text{đơn vị: } \text{kg } BOD_5/m^3\cdot d \text{ hoặc } \text{kg } COD/m^3\cdot d)$$
- Mối liên hệ chuyển đổi trực tiếp:
  $$OLR = (F/M) \times X_{\text{MLVSS}} \times 10^{-3}$$
- Tiêu chuẩn thiết kế:
  - CMAS thông thường: $OLR = 0.3 - 1.2\ \text{kg } BOD_5/m^3\cdot d$
  - Làm thoáng kéo dài: $OLR = 0.1 - 0.3\ \text{kg } BOD_5/m^3\cdot d$

---

#### 4.4 Các Chỉ tiêu Chất rắn Lơ lửng trong Bể phản ứng (MLSS, MLVSS, Ash Content)

##### 4.4.1 Hỗn hợp bùn lỏng (Mixed Liquor Suspended Solids - MLSS & MLVSS)
- **$MLSS$ (Mixed Liquor Suspended Solids):** Tổng hàm lượng chất rắn lơ lửng có trong bể aerotank, đo bằng cách lọc mẫu qua giấy lọc sợi thủy tinh $0.45 - 1.2\ \mu\text{m}$ và sấy khô ở $103 - 105^\circ\text{C}$ ($mg/L$).
- **$MLVSS$ (Mixed Liquor Volatile Suspended Solids):** Phần chất rắn bay hơi bị đốt cháy ở $550 \pm 50^\circ\text{C}$, đại diện cho phần hữu cơ vi sinh vật ($mg/L$).
- **Hàm lượng khoáng tro (Fixed Suspended Solids - FSS / Ash):**
  $$FSS = MLSS - MLVSS$$
- Tỷ số $MLVSS / MLSS$:
  - Nước thải sinh hoạt thông thường: $MLVSS / MLSS = 0.75 - 0.85$ (trung bình thiết kế: $0.80$).
  - Nước thải nhiều cặn vô cơ (cát mịn, muối khoáng): $MLVSS / MLSS = 0.60 - 0.70$.
  - Khi tỷ số này sụt giảm bất thường ($< 0.65$), hệ thống đang bị nhiễm cặn khoáng hoặc bùn quá già dẫn đến khoáng hóa cao.

##### 4.4.2 Cấu trúc 3 thành phần phân rã của MLVSS ($X_T$)
- Trong mô hình sinh học hiện đại (ASM1, Metcalf & Eddy), tổng $MLVSS$ ($X_T$) gồm 3 hợp phần tách biệt:
  $$X_T = X_b + X_d + X_i$$
  - $X_b$: Sinh khối vi khuẩn dị dưỡng sống hoạt tính ($Active\ biomass$, $mg/L$):
    $$X_b = \left(\frac{SRT}{\theta}\right) \left[\frac{Y (S_0 - S)}{1 + b \cdot SRT}\right]$$
  - $X_d$: Mảnh vụn tế bào trơ tích lũy từ quá trình phân hủy nội sinh ($Endogenous\ cell\ debris$, $mg/L$):
    $$X_d = f_d \cdot b \cdot X_b \cdot SRT \quad (f_d \approx 0.10 - 0.15)$$
  - $X_i$: Chất rắn lơ lửng hữu cơ trơ không phân hủy sinh học từ nước thải đầu vào tích tụ lại ($Influent\ non\text{-}biodegradable\ VSS$, $mg/L$):
    $$X_i = X_{0,i} \cdot \left(\frac{SRT}{\theta}\right)$$
- Tỷ lệ sinh khối hoạt tính thực sự ($f_{\text{act}} = X_b / X_T$):
  - Ở $SRT = 3 - 5\ \text{ngày}$: $f_{\text{act}} \approx 60 - 75\%$.
  - Ở $SRT = 15 - 30\ \text{ngày}$: $f_{\text{act}} \approx 30 - 45\%$ (phần lớn bùn là cell debris và cặn trơ).

---

### 5. Bài tập Thiết kế và Ví dụ Tính toán Điển hình Từng bước (Step-by-Step Worked Examples)

#### 5.1 Ví dụ Tính toán 1: Xác định Chỉ số Thể tích Bùn (SVI) và Đánh giá Khả năng Lắng

##### 5.1.1 Đề bài
> Tại một trạm xử lý nước thải công nghiệp thực phẩm, kỹ sư lấy mẫu hỗn hợp bùn lỏng từ cuối bể hiếu khí để tiến hành thí nghiệm lắng tĩnh trong ống đong hình trụ tiêu chuẩn $1000\ \text{mL}$.
> - Sau $30\ \text{phút}$ lắng tĩnh, ranh giới bùn dừng ở vạch chia $280\ \text{mL}$.
> - Kết quả phân tích phòng thí nghiệm xác định nồng độ $MLSS = 2800\ \text{mg/L}$ và $MLVSS = 2240\ \text{mg/L}$.
> 
> **Yêu cầu:**
> 1. Tính toán chỉ số thể tích bùn $SVI$ của hệ thống.
> 2. Đưa ra chẩn đoán kỹ thuật về đặc tính lắng của bùn và chất lượng bông bùn.
> 3. Trong tuần vận hành tiếp theo, do sự cố tăng tải trọng hữu cơ, thể tích lắng sau $30\ \text{phút}$ tăng vọt lên $SV_{30} = 620\ \text{mL}$ trong khi $MLSS$ giảm nhẹ còn $2400\ \text{mg/L}$. Hãy tính lại $SVI$, xác định nguy cơ sự cố và đề xuất 2 hành động can thiệp tức thời.

##### 5.1.2 Các thông số đã cho
- Thể tích lắng ban đầu: $SV_{30,1} = 280\ \text{mL/L}$
- Nồng độ chất rắn ban đầu: $MLSS_1 = 2800\ \text{mg/L} = 2.80\ \text{g/L}$
- Thể tích lắng khi gặp sự cố: $SV_{30,2} = 620\ \text{mL/L}$
- Nồng độ chất rắn khi gặp sự cố: $MLSS_2 = 2400\ \text{mg/L} = 2.40\ \text{g/L}$

##### 5.1.3 Lời giải chi tiết từng bước

###### Bước 1: Tính toán chỉ số SVI ban đầu
- Áp dụng công thức tiêu chuẩn:
  $$SVI_1 = \frac{SV_{30,1} \times 1000}{MLSS_1}$$
- Thay số:
  $$SVI_1 = \frac{280\ \text{mL/L} \times 1000\ \text{mg/g}}{2800\ \text{mg/L}} = 100.0\ \text{mL/g}$$

###### Bước 2: Chẩn đoán kỹ thuật trạng thái ban đầu
- Giá trị $SVI_1 = 100.0\ \text{mL/g}$ nằm chính giữa khoảng tối ưu lý tưởng ($80 - 150\ \text{mL/g}$).
- Tỷ số $MLVSS / MLSS = 2240 / 2800 = 0.80$ đạt giá trị tiêu chuẩn hoàn hảo.
- Kết luận: Bông bùn có cấu trúc cân đối giữa vi khuẩn tạo bông và vi khuẩn dạng sợi; tốc độ lắng khối nhanh, ranh giới lắng sắc nét, nước trong sau lắng đạt độ trong suốt cao, không có nguy cơ trào bùn.

###### Bước 3: Tính toán chỉ số SVI khi xảy ra biến động
- Áp dụng công thức khi gặp sự cố:
  $$SVI_2 = \frac{SV_{30,2} \times 1000}{MLSS_2} = \frac{620 \times 1000}{2400} = 258.33\ \text{mL/g}$$

###### Bước 4: Đánh giá nguy cơ và Giải pháp can thiệp khẩn cấp
- **Đánh giá:**
  - $SVI_2 = 258.33\ \text{mL/g} > 200\ \text{mL/g}$: Hệ thống đã rơi vào tình trạng **Phình bùn nghiêm trọng (Severe Sludge Bulking)**. Khả năng nén của bùn suy giảm nghiêm trọng, lớp bùn đáy bể lắng sẽ nở rộng thể tích và trào qua máng thu nước trong nếu lưu lượng đỉnh xuất hiện.
- **Biện pháp can thiệp tức thời:**
  1. *Khử trùng chọn lọc dòng bùn tuần hoàn ($RAS$):* Châm hóa chất $\text{NaOCl}$ hoặc khí Clo vào đường ống $RAS$ với liều lượng $3.0 - 4.0\ \text{kg } Cl_2 / 1000\ \text{kg } MLSS\cdot d$ trong vòng $48 - 72\ \text{giờ}$ để đốt cháy các sợi vi khuẩn vươn dài ra ngoài bông bùn.
  2. *Kiểm tra và nâng DO bể hiếu khí:* Tăng công suất quạt gió nâng nồng độ $DO$ lên $\ge 2.5 - 3.0\ \text{mg/L}$ để triệt tiêu ưu thế cạnh tranh của các chủng vi khuẩn sợi chịu oxy thấp (*S. natans*, Type 1701).

---

#### 5.2 Ví dụ Tính toán 2: Tính toán F/M, SRT và Lưu lượng Bùn Xả (WAS Flow Rate)

##### 5.2.1 Đề bài
> Một trạm xử lý nước thải đô thị quy mô tập trung tiếp nhận lưu lượng thiết kế $Q = 15,000\ m^3/d$ với hàm lượng $BOD_5$ đầu vào bể sinh học $S_0 = 220\ mg/L$.
> Công trình gồm 2 nguyên đơn bể hiếu khí hoàn toàn xáo trộn ($CMAS$) hoạt động song song với tổng dung tích hữu ích $V = 3,750\ m^3$.
> Số liệu phân tích kiểm soát vận hành:
> - Nồng độ hỗn hợp bùn lỏng: $MLSS = 3,000\ mg/L$, tỷ số $MLVSS / MLSS = 0.80$.
> - Nồng độ bùn hoạt tính tuần hoàn từ đáy bể lắng đợt 2: $X_R = 8,500\ mg/L$ (tỷ lệ bay hơi cũng là $80\%$).
> - Nồng độ chất rắn lơ lửng trong nước đầu ra sau lắng đợt 2: $TSS_e = 12\ mg/L$ ($VSS_e = 9.6\ mg/L$).
> - Yêu cầu chế độ công nghệ duy trì tuổi bùn: $SRT = 8.0\ \text{ngày}$.
> 
> **Yêu cầu:**
> 1. Tính thời gian lưu nước thủy lực ($HRT$) của bể hiếu khí (tính bằng giờ).
> 2. Tính tỷ số $F/M$ theo $MLVSS$ ($kg\ BOD_5 / kg\ MLVSS\cdot d$).
> 3. Tính tổng khối lượng bùn hoạt tính ($MLSS$ và $MLVSS$) có trong bể hiếu khí ($kg$).
> 4. Tính lưu lượng xả bùn dư mỗi ngày ($Q_w$, $m^3/d$) từ đáy bể lắng đợt 2 để duy trì đúng $SRT = 8.0\ \text{ngày}$.
> 5. Nếu trạm thay đổi thiết kế xả bùn trực tiếp từ bể hiếu khí, lưu lượng xả $Q_w'$ cần thiết là bao nhiêu?

##### 5.2.2 Các thông số đã cho
- $Q = 15,000\ m^3/d$
- $S_0 = 220\ mg/L = 220\ g/m^3$
- $V = 3,750\ m^3$
- $MLSS = 3,000\ mg/L = 3.0\ kg/m^3$
- $X_{\text{MLVSS}} = 3,000 \times 0.80 = 2,400\ mg/L = 2.40\ kg/m^3$
- $X_{w,\text{MLSS}} = X_R = 8,500\ mg/L = 8.50\ kg/m^3$
- $X_{w,\text{MLVSS}} = 8,500 \times 0.80 = 6,800\ mg/L = 6.80\ kg/m^3$
- $X_e = 12\ mg/L = 0.012\ kg/m^3$
- $X_{e,\text{VSS}} = 9.6\ mg/L = 0.0096\ kg/m^3$
- $SRT = \theta_c = 8.0\ \text{ngày}$

##### 5.2.3 Lời giải chi tiết từng bước

###### Bước 1: Tính thời gian lưu nước thủy lực (HRT)
- Biểu thức:
  $$HRT = \frac{V}{Q}$$
- Thay số:
  $$HRT = \frac{3,750\ m^3}{15,000\ m^3/d} = 0.25\ \text{ngày} = 0.25 \times 24\ \text{h} = 6.0\ \text{giờ}$$

###### Bước 2: Tính tỷ số thức ăn trên vi sinh vật (F/M)
- Biểu thức:
  $$F/M = \frac{Q \cdot S_0}{V \cdot X_{\text{MLVSS}}}$$
- Thay số:
  $$F/M = \frac{15,000\ m^3/d \times 220\ g/m^3}{3,750\ m^3 \times 2,400\ g/m^3} = \frac{3,300,000\ g\ BOD_5/d}{9,000,000\ g\ MLVSS} = 0.367\ \text{kg } BOD_5 / \text{kg } MLVSS\cdot d$$
- Nhận xét: Giá trị $F/M = 0.367\ \text{d}^{-1}$ nằm hoàn toàn trong khoảng thiết kế chuẩn của bể CMAS ($0.20 - 0.60\ \text{d}^{-1}$).

###### Bước 3: Tính tổng khối lượng bùn trong bể hiếu khí
- Tổng khối lượng $MLSS$:
  $$M_{\text{MLSS}} = V \times MLSS = 3,750\ m^3 \times 3.0\ kg/m^3 = 11,250\ \text{kg } MLSS$$
- Tổng khối lượng $MLVSS$:
  $$M_{\text{MLVSS}} = V \times X_{\text{MLVSS}} = 3,750\ m^3 \times 2.40\ kg/m^3 = 9,000\ \text{kg } MLVSS$$

###### Bước 4: Xác định lưu lượng xả bùn đáy bể lắng ($Q_w$)
- Áp dụng phương trình cân bằng $SRT$ tính theo hệ $MLSS$:
  $$SRT = \frac{V \cdot MLSS}{(Q - Q_w) X_e + Q_w X_w}$$
  - Trong đó lượng cặn thất thoát theo nước đầu ra:
    $$P_{\text{effluent}} = (Q - Q_w) \times X_e \approx Q \times X_e = 15,000\ m^3/d \times 0.012\ kg/m^3 = 180\ \text{kg } TSS/d$$
- Tổng khối lượng bùn cần loại bỏ khỏi hệ thống mỗi ngày để duy trì $SRT = 8.0\ \text{ngày}$:
  $$P_{\text{total, waste}} = \frac{M_{\text{MLSS}}}{SRT} = \frac{11,250\ \text{kg}}{8.0\ \text{ngày}} = 1,406.25\ \text{kg } TSS/d$$
- Lượng bùn cần xả cưỡng bức qua trạm bơm bùn dư ($WAS$):
  $$P_{\text{WAS}} = P_{\text{total, waste}} - P_{\text{effluent}} = 1,406.25 - 180 = 1,226.25\ \text{kg } TSS/d$$
- Vì lượng bùn này được rút từ đáy bể lắng với nồng độ $X_w = 8.50\ kg/m^3$:
  $$Q_w = \frac{P_{\text{WAS}}}{X_w} = \frac{1,226.25\ \text{kg/d}}{8.50\ kg/m^3} = 144.26\ m^3/d$$
- *Kiểm tra chính xác bằng nghiệm đại số:*
  $$8.0 = \frac{11,250}{(15,000 - Q_w) \times 0.012 + Q_w \times 8.50} = \frac{11,250}{180 - 0.012 Q_w + 8.50 Q_w} = \frac{11,250}{180 + 8.488 Q_w}$$
  $$180 + 8.488 Q_w = \frac{11,250}{8.0} = 1,406.25 \Rightarrow 8.488 Q_w = 1,226.25 \Rightarrow Q_w = 144.47\ m^3/d$$
  *(Chênh lệch không đáng kể $\approx 0.1\%$). Kết quả thiết kế lấy $Q_w = 144.5\ m^3/d$.*

###### Bước 5: Tính lưu lượng xả bùn trực tiếp từ bể hiếu khí ($Q_w'$)
- Khi xả trực tiếp từ bể hiếu khí, nồng độ bùn xả là $MLSS = 3.0\ kg/m^3$:
  $$Q_w' = \frac{P_{\text{WAS}}}{MLSS} = \frac{1,226.25\ \text{kg/d}}{3.0\ kg/m^3} = 408.75\ m^3/d$$
- Nếu bỏ qua cặn trôi ra máng thu ($X_e \approx 0$):
  $$Q_{w,\text{ideal}}' = \frac{V}{SRT} = \frac{3,750\ m^3}{8.0\ \text{d}} = 468.75\ m^3/d$$

---

#### 5.3 Ví dụ Chẩn đoán 3: Diễn giải Hình ảnh Soi kính Hiển vi Vi sinh và Phác đồ Xử lý Sự cố Bùn hoạt tính

##### 5.3.1 Mô tả hiện trường và Triệu chứng lâm sàng
> Tại nhà máy xử lý nước thải dệt nhuộm công suất $8,000\ m^3/d$, trong 3 ngày qua xuất hiện các hiện tượng bất thường:
> - Nước trên bể lắng đợt 2 bị đục nhẹ, lớp ranh giới bùn dâng cao chỉ cách mép máng thu $0.4\ \text{m}$ (bình thường là $1.8\ \text{m}$).
> - Thí nghiệm ống đong ghi nhận $SV_{30}$ tăng từ $260\ \text{mL/L}$ lên $580\ \text{mL/L}$, nồng độ $MLSS = 2,900\ mg/L \rightarrow SVI = 200\ mL/g$.
> - Cán bộ kỹ thuật lấy mẫu bùn tươi soi dưới kính hiển vi quang học độ phóng đại $100\times, 400\times, 1000\times$ và thực hiện các thử nghiệm nhuộm:
>   - Quan sát thấy các sợi vi khuẩn vươn dài chằng chịt giữa các bông bùn, tạo cầu nối không cho các bông bùn tiếp cận nhau.
>   - Nhuộm Gram: Các sợi có kết quả **Gram âm ($\text{Gram}^-$)**.
>   - Nhuộm Neisser: Không bắt màu xanh tím, kết quả **Neisser âm ($\text{Neisser}^-$)**.
>   - Quan sát hình thái tế bào: Sợi có vỏ bao (sheath) dạng ống rõ rệt, bên trong chứa các tế bào hình que xếp thành chuỗi, không có các hạt lưu huỳnh nội bào.
>   - Quần xã động vật nguyên sinh: Trùng lông có cuống (*Vorticella*) thưa thớt và co cụm cuống; trùng roi nhỏ (*Bodo*) xuất hiện với mật độ khá cao.
> - Dữ liệu đo đạc online: Máy đo DO tại ngăn cuối bể aerotank hiển thị $DO = 0.55\ mg/L$.

##### 5.3.2 Phác đồ 5 bước Chẩn đoán và Xử lý Chuẩn kỹ thuật

###### Bước 1: Nhận diện định danh vi sinh vật gây hại
- Căn cứ vào khóa phân loại vi khuẩn dạng sợi Eikelboom & Jenkins:
  - Hình thái sợi có vỏ bọc dạng ống ($sheathed$), tế bào hình que xếp chuỗi.
  - Phản ứng nhuộm: $\text{Gram}^-$, $\text{Neisser}^-$, không chứa hạt lưu huỳnh nội bào.
  - $\rightarrow$ **Định danh chính xác loài:** ***Sphaerotilus natans***.
- Sự suy giảm trùng lông có cuống và ưu thế trùng roi khẳng định môi trường đang bị thiếu hụt oxy nghiêm trọng và chuyển dịch về trạng thái tải hữu cơ không cân bằng.

###### Bước 2: Xác định nguyên nhân gốc rễ (Root Cause Analysis)
- Loài *Sphaerotilus natans* là vi khuẩn chỉ thị số 1 cho hiện tượng **Thiếu hụt oxy hòa tan ($Low\ DO\ Bulking$)**.
- Giá trị $DO = 0.55\ mg/L$ ở cuối bể hiếu khí thấp hơn nhiều so với ngưỡng kiểm soát an toàn tối thiểu ($2.0\ mg/L$). Kiểm tra hệ thống cấp khí phát hiện màng đĩa phân phối khí bị nghẹt một phần và van cấp khí nhánh bị kẹt mở $30\%$.

###### Bước 3: Phác đồ can thiệp cấp bách (Emergency Response - Trong vòng 24 đến 48 giờ)
1. **Khắc phục cấp khí:** Mở van nhánh cấp khí khẩn cấp, huy động máy thổi khí dự phòng, đưa nồng độ $DO$ trong toàn bộ bể aerotank lên dải $2.5 - 3.5\ mg/L$.
2. **Khử trùng chọn lọc dòng RAS (Chlorination):**
   - Tổng khối lượng bùn trong hệ thống:
     $$M_{\text{system}} \approx V \times MLSS = 2,500\ m^3 \times 2.9\ kg/m^3 = 7,250\ kg\ MLSS$$
   - Liều châm Clo mục tiêu: $3.0\ kg\ Cl_2 / 1000\ kg\ MLSS\cdot d$.
   - Lượng Clo hoạt tính nguyên chất cần châm mỗi ngày:
     $$W_{\text{Cl2}} = 7,250\ kg \times \frac{3.0\ kg}{1000\ kg\cdot d} = 21.75\ kg\ Cl_2/d$$
   - Nếu sử dụng dung dịch $\text{NaOCl}$ công nghiệp nồng độ $10\%$ ($\rho = 1.15\ kg/L$, chứa $115\ g\ Cl_2/L$):
     $$V_{\text{NaOCl}} = \frac{21,750\ g}{115\ g/L} \approx 189.1\ L/d \approx 7.88\ L/h$$
   - Cài đặt bơm định lượng châm liên tục $7.9\ L/h$ dung dịch $\text{NaOCl}\ 10\%$ vào giếng thu bùn tuần hoàn $RAS$.

###### Bước 4: Theo dõi và Đánh giá hiệu quả lâm sàng (Clinical Monitoring)
- Đo kiểm $SV_{30}$ mỗi $4\ \text{giờ}$ một lần.
- Lấy mẫu soi kính hiển vi mỗi $12\ \text{giờ}$:
  - Sau $24\ \text{giờ}$: Các sợi *Sphaerotilus natans* bắt đầu đứt đoạn, vỏ bao bị rách, tế bào co rút.
  - Sau $48\ \text{giờ}$: Đa số sợi bị phân hủy rỗng ruột, chỉ số $SVI$ hạ từ $200\ mL/g$ xuống $140\ mL/g$.
  - Khi $SVI \le 130\ mL/g$: Ngừng châm Clo ngay lập tức để tránh làm tổn thương sâu đến vi khuẩn nitrat hóa và vi khuẩn tạo bông.

###### Bước 5: Giải pháp căn cơ dài hạn (Permanent Prevention)
1. Lắp đặt hệ thống điều khiển tự động lưu lượng khí thổi theo thuật toán PID liên động với đầu đo DO quang học (Optical DO sensor), cài đặt Setpoint cố định $DO = 2.0\ mg/L$.
2. Cải tạo ngăn đầu dòng bể aerotank thành một **Bể chọn lọc hiếu khí (Aerobic Selector)** với $HRT = 20\ \text{phút}$ để tạo gradient nồng độ cơ chất mạnh, ức chế vĩnh viễn sự tái phát của *Sphaerotilus natans*.
