import { Component } from '@angular/core';
import { ApiService } from '../service/api.service';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {

  prediction: string = '';
  selectedFile: File | null = null;  
  uploadResponse:string = '';
  isUploading:boolean = false;

  constructor(private apiService: ApiService) { }

  onFileSelected(event: any): void {
    const file = event.target.files[0];
    if (file) {
      this.selectedFile = file;  
    }
  }

  onUpload(): void {
    if (this.selectedFile) {
      this.uploadImage(this.selectedFile);  
    } else {
      console.error('selecciona un archivo primero');
    }
  }


  
  uploadImage(file: File) {
    const formData = new FormData();
    formData.append('file', file, file.name);

    this.apiService.uploadImage(formData).subscribe(
      response => {
        this.isUploading = false;
        this.prediction = response.Prediction?.prediction;  
        
        
        this.uploadResponse = 'Imagen subida' + JSON.stringify(response);

        console.log('Imagen subida', response);
      },
      error => {
        this.uploadResponse = 'Error al subir imagen' + JSON.stringify(error);
        this.isUploading = false;
        console.error('Error al subir imagen', error);
      }
    );
  }
  


}
