import apiClient from '@/http-common';
import type Face from '@/types/Face';

class FaceService {
  search(image: File): Promise<any> {
    const formData = new FormData();

    formData.append('image', image);

    return apiClient.post('/search', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
  }
  upload(image: File, data: Face): Promise<any> {
    const formData = new FormData();

    formData.append('image', image);
    formData.append('data', JSON.stringify(data));

    return apiClient.post('/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
  }
}

export default new FaceService();
