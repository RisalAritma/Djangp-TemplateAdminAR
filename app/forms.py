from django import forms
from .models import UserProfile, Faculty


STATUS_CHOICES = [
    ('Dosen', 'Dosen'),
    ('Tenaga Kependidikan', 'Tenaga Kependidikan'),
    ('Mahasiswa', 'Mahasiswa'),
]

GENDER_CHOICES = [
    ('Laki-laki', 'Laki-laki'),
    ('Perempuan', 'Perempuan'),
]

GENERATION_CHOICES = [
    ('Baby Boomer', 'Baby Boomer (Kelahiran 1946-1964)'),
    ('Gen X', 'Gen X (Kelahiran 1965-1980)'),
    ('Millennial', 'Millennial (Kelahiran 1981-1996)'),
    ('Gen Z', 'Gen Z (Kelahiran 1997-2012)'),
]


class DemografiForm(forms.ModelForm):

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,
        label='Jenis Kelamin',
        required=True
    )

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.RadioSelect,
        label='Status',
        required=True
    )

    generation = forms.ChoiceField(
        choices=GENERATION_CHOICES,
        widget=forms.RadioSelect,
        label='Generasi Usia',
        required=True
    )

    inst_faculty = forms.ModelChoiceField(
        queryset=Faculty.objects.select_related(
            'institution'
        ).order_by(
            'institution__name',
            'name'
        ),
        label='Pilih Fakultas',
        required=True,
        empty_label='Pilih Universitas / Fakultas',
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

    class Meta:

        model = UserProfile

        fields = [
            'gender',
            'generation',
            'status',
            'inst_faculty'
        ]

class QEE_Form(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'q_ee_1',
            'q_ee_2',
            'q_ee_3',
        ]
        widgets = {
            'q_ee_1': forms.RadioSelect(choices=[
                ('Pernah', 'Pernah'),
                ('Jarang', 'Jarang'),
                ('Kadang-kadang', 'Kadang-kadang'),
                ('Cukup Sering', 'Cukup Sering'),
                ('Sering', 'Sering'),
            ],attrs={'required': True}),
            'q_ee_2': forms.RadioSelect(choices=[
                ('Pernah', 'Pernah'),
                ('Jarang', 'Jarang'),
                ('Kadang-kadang', 'Kadang-kadang'),
                ('Cukup Sering', 'Cukup Sering'),
                ('Sering', 'Sering'),
            ],attrs={'required': True}),
            'q_ee_3': forms.RadioSelect(choices=[
                ('Pernah', 'Pernah'),
                ('Jarang', 'Jarang'),
                ('Kadang-kadang', 'Kadang-kadang'),
                ('Cukup Sering', 'Cukup Sering'),
                ('Sering', 'Sering'),
            ],attrs={'required': True}),
        }

class QIE_Form(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'q_ie_1',
            'q_ie_2',
            'q_ie_3',
            'q_ie_4',
            'q_ie_5',
            'q_ie_6',
            'q_ie_7',
            'q_ie_8',
        ]
        widgets = {
            'q_ie_1': forms.RadioSelect(choices=[
                ('Ya', 'Ya'),
                ('Tidak', 'Tidak'),
            ],attrs={'required': True}),
            'q_ie_2': forms.RadioSelect(choices=[
                ('Ya', 'Ya'),
                ('Tidak', 'Tidak'),
            ],attrs={'required': True}),
            'q_ie_3': forms.RadioSelect(choices=[
                ('Ya', 'Ya'),
                ('Tidak', 'Tidak'),
            ],attrs={'required': True}),
            'q_ie_4': forms.RadioSelect(choices=[
                ('Ya', 'Ya'),
                ('Tidak', 'Tidak'),
            ],attrs={'required': True}),
            'q_ie_5': forms.RadioSelect(choices=[
                ('Ya', 'Ya'),
                ('Tidak', 'Tidak'),
            ],attrs={'required': True}),
            'q_ie_6': forms.RadioSelect(choices=[
                ('Tidak pernah ', 'Tidak pernah '),
                ('Jarang', 'Jarang'),
                ('Kadang-kadang', 'Kadang-kadang'),
                ('Cukup Sering', 'Cukup Sering'),
                ('Sering', 'Sering'),
            ],attrs={'required': True}),
            'q_ie_7': forms.RadioSelect(choices=[
                ('Media sosial kampus', 'Media sosial kampus'),
                ('Website kampus', 'Website kampus'),
                ('Email resmi kampus', 'Email resmi kampus'),
                ('Dosen/atasan', 'Dosen/atasan'),
                ('Teman atau rekan kampus', 'Teman atau rekan kampus'),
                ('Kegiatan sosialisasi/seminar', 'Kegiatan sosialisasi/seminar'),
                ('Satgas atau layanan kampus', 'Satgas atau layanan kampus'),
                ('Grup WhatsApp/Telegram', 'Grup WhatsApp/Telegram'),
                ('Belum pernah memperoleh informasi', 'Belum pernah memperoleh informasi'),
                ('Lainnya', 'Lainnya'),
            ],attrs={'required': True}),
            'q_ie_8': forms.RadioSelect(choices=[
                ('Sangat Sulit', 'Sangat Sulit'),
                ('Sulit', 'Sulit'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Mudah', 'Mudah'),
                ('Sangat Mudah', 'Sangat Mudah'),
            ],attrs={'required': True}),
        }
        


class QAA_Form(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'q_aa_1',
            'q_aa_2',
            'q_aa_3',
            'q_aa_4',
            'q_aa_5',
        ]
        widgets = {
            'q_aa_1': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_aa_2': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_aa_3': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_aa_4': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_aa_5': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
        }



class QPRS_Form(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'q_prs_1',
            'q_prs_2',
            'q_prs_3',
            'q_prs_4',
            'q_prs_5',
        ]
        widgets = {
            'q_prs_1': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_prs_2': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_prs_3': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_prs_4': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_prs_5': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
        }




class QIT_Form(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'q_it_1',
            'q_it_2',
            'q_it_3',
            'q_it_4',
            'q_it_5',
            'q_it_6',
            'q_it_7',
            'q_it_8',
        ]
        widgets = {
            'q_it_1': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_it_2': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_it_3': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_it_4': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_it_5': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_it_6': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_it_7': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_it_8': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
        }


class QPRF_Form(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'q_prf_1',
            'q_prf_2',
            'q_prf_3',
            'q_prf_4',
            'q_prf_5',
            'q_prf_6',
        ]
        widgets = {
            'q_prf_1': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_prf_2': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_prf_3': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_prf_4': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_prf_5': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_prf_6': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
        }


class QCC_Form(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'q_cc_1',
            'q_cc_2',
            'q_cc_3',
            'q_cc_4',
            'q_cc_5',
        ]
        widgets = {
            'q_cc_1': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_cc_2': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_cc_3': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_cc_4': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
            'q_cc_5': forms.RadioSelect(choices=[
                ('Sangat Setuju', 'Sangat Setuju'),
                ('Setuju', 'Setuju'),
                ('Ragu-ragu', 'Ragu-ragu'),
                ('Tidak Setuju', 'Tidak Setuju'),
                ('Sangat Tidak Setuju', 'Sangat Tidak Setuju'),
            ],attrs={'required': True}),
        }
     