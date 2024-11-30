import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-data-container',
  standalone: true,
  imports: [],
  templateUrl: './data-container.component.html',
  styleUrl: './data-container.component.scss'
})
export class DataContainerComponent{

  @Input() title : string = '';
  @Input() content : string = '';
  @Input() type : string = '';

}
