# Generated by Django 3.1 on 2020-08-31 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataPerusahaan',
            fields=[
                ('id_data_perusahaan', models.AutoField(primary_key=True, serialize=False)),
                ('nama_perusahaan', models.CharField(max_length=255)),
                ('akta_pendirian_badan_usaha', models.FileField(upload_to='akta_pendirian_badan_usaha')),
                ('nama_pemilik', models.CharField(max_length=255)),
                ('foto_pemilik', models.ImageField(upload_to='foto_pemilik')),
                ('ktp_pemilik', models.FileField(upload_to='ktp_pemilik')),
                ('bentuk_perusahaan', models.CharField(max_length=20)),
                ('alamat_perusahaan', models.CharField(max_length=255)),
                ('tahun_berdiri', models.IntegerField()),
                ('no_telp', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(max_length=255)),
                ('verified_admin', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DataProyek',
            fields=[
                ('id_data_proyek', models.AutoField(primary_key=True, serialize=False)),
                ('lokasi_proyek', models.CharField(max_length=255)),
                ('luas_total_area_proyek', models.FloatField()),
                ('jumlah_total_unit', models.IntegerField()),
                ('jenis_produk', models.CharField(max_length=50)),
                ('jumlah_tipe_rumah', models.IntegerField()),
                ('target_pembangunan', models.IntegerField()),
                ('verified_tipe_rumah', models.BooleanField(default=False)),
                ('verified_jenis_psu', models.BooleanField(default=False)),
                ('verified_data_perizinan', models.BooleanField(default=False)),
                ('verified_admin_data_proyek', models.PositiveSmallIntegerField(default=0)),
                ('verified_admin_tipe_rumah', models.PositiveSmallIntegerField(default=0)),
                ('verified_admin_jenis_psu', models.PositiveSmallIntegerField(default=0)),
                ('verified_admin_data_perizinan', models.PositiveSmallIntegerField(default=0)),
                ('id_data_perusahaan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pelaporan.dataperusahaan')),
            ],
        ),
        migrations.CreateModel(
            name='DataPerizinan',
            fields=[
                ('id_data_proyek', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pelaporan.dataproyek')),
                ('site_plan', models.FileField(upload_to='site_plan')),
                ('ukl_upl', models.FileField(upload_to='ukl_upl')),
                ('izin_mendirikan_bangunan', models.FileField(upload_to='izin_mendirikan_bangunan')),
                ('izin_penggunaan_bangunan', models.FileField(upload_to='izin_penggunaan_bangunan')),
            ],
        ),
        migrations.CreateModel(
            name='JenisPsu',
            fields=[
                ('id_data_proyek', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pelaporan.dataproyek')),
                ('jaringan_jalan', models.FloatField(default=0)),
                ('jaringan_saluran_pembuangan_air_hujan', models.FloatField(default=0)),
                ('sanitasi', models.FloatField(default=0)),
                ('jaringan_saluran_pembuangan_air_limbah', models.FloatField(default=0)),
                ('tempat_pembuangan_sampah', models.FloatField(default=0)),
                ('sarana_perniagaan', models.FloatField(default=0)),
                ('sarana_pelayanan_umum_dan_pemerintahan', models.FloatField(default=0)),
                ('sarana_pendidikan', models.FloatField(default=0)),
                ('sarana_kesehatan', models.FloatField(default=0)),
                ('sarana_peribadatan', models.FloatField(default=0)),
                ('sarana_rekreasi_dan_olahraga', models.FloatField(default=0)),
                ('sarana_pemakaman', models.FloatField(default=0)),
                ('sarana_pertanaman_dan_ruang_terbuka_hijau', models.FloatField(default=0)),
                ('sarana_parkir', models.FloatField(default=0)),
                ('jaringan_air_bersih', models.FloatField(default=0)),
                ('jaringan_listrik', models.FloatField(default=0)),
                ('jaringan_telepon', models.FloatField(default=0)),
                ('jaringan_gas', models.FloatField(default=0)),
                ('jaringan_transportasi', models.FloatField(default=0)),
                ('pemadam_kebakaran', models.FloatField(default=0)),
                ('sarana_penerangan_jalan_umum', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RumahTapak',
            fields=[
                ('id_rumah_tapak', models.AutoField(primary_key=True, serialize=False)),
                ('tipe_rumah_tapak', models.IntegerField()),
                ('lb_rumah_tapak', models.FloatField()),
                ('lt_rumah_tapak', models.FloatField()),
                ('jumlah_unit_rumah_tapak', models.IntegerField()),
                ('id_data_proyek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pelaporan.dataproyek')),
            ],
        ),
        migrations.CreateModel(
            name='RumahSusun',
            fields=[
                ('id_rumah_susun', models.AutoField(primary_key=True, serialize=False)),
                ('tipe_rumah_susun', models.IntegerField()),
                ('lb_rumah_susun', models.FloatField()),
                ('jumlah_unit_rumah_susun', models.IntegerField()),
                ('id_data_proyek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pelaporan.dataproyek')),
            ],
        ),
        migrations.CreateModel(
            name='Notifikasi',
            fields=[
                ('id_notifikasi', models.AutoField(primary_key=True, serialize=False)),
                ('isi_notifikasi', models.TextField()),
                ('id_data_perusahaan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pelaporan.dataperusahaan')),
            ],
        ),
    ]
