from django.test import TestCase
from pelaporan.models import DataPerusahaan
from admin_pelaporan.models import get_nama_perusahaan
from unittest.mock import Mock, patch

class AdminTest(TestCase):

    @patch('pelaporan.models.DataPerusahaan.objects')
    def testing_get_nama_perusahaan(self, mock_get_nama_perusahaan):
        mockObject = Mock(spec=DataPerusahaan)
        mockObject.id_data_perusahaan = 1
        mockObject.nama_perusahaan = 'Patrick Industries Testing'
        mockObject.nama_pemilik = 'Patrick'
        mockObject.bentuk_perusahaan = 'CV'
        mockObject.alamat_perusahaan = 'Alamat Testing'
        mockObject.tahun_berdiri = 1999
        mockObject.no_telp = '081000000000'
        mockObject.email = 'testing26@gmail.com'
        mockObject.website = 'www.patrickindustries.com'
        mockObject.verified_admin = 0

        mockObject.foto_pemilik = 'Testing Folder/testing.jpg'
        mockObject.ktp_pemilik = 'Testing Folder/testing.pdf'
        mockObject.akta_pendirian_badan_usaha = 'Testing Folder/testing.pdf'

        mock_get_nama_perusahaan.get.return_value = mockObject
        
        id = mockObject.id_data_perusahaan
        expected = 'Patrick Industries Testing'
        actual = get_nama_perusahaan(id)
        print('HASIL NAMA PERUSAHAAN: ' + actual)
        self.assertEqual(expected, actual)