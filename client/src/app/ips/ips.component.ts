import { Component, OnInit } from '@angular/core';
import { TraficService } from '../trafic.service';
declare var $: any;

@Component({
  selector: 'app-ips',
  templateUrl: './ips.component.html',
  styleUrls: ['./ips.component.css']
})
export class IpsComponent implements OnInit {



  constructor(private traficService: TraficService) { }

  adresses = [];

  ngOnInit() {
    $(document).ready(() => {
      $('#example').DataTable({
        "order": [[2, "desc"]]
      });
    });

    this.traficService.getIps()
      .subscribe(
        (data: string) => {
          console.log(data);
          this.adresses = JSON.parse(data);
        },
        err => {
          console.error(err);
        }
      );
  }

}
